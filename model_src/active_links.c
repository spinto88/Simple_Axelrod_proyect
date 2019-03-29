#include "active_links.h"

int active_condition(mysys *msys, int i, int j, double delta)
{
        if(msys->a[i][j] == 1)
        {
                if((msys->corr[i][j] > (delta * 0.5)) && (msys->corr[i][j] < 1.00))
                        return 1;
        }

        return 0;
}

int number_of_active_links(mysys *msys, double delta)
{
	int i,j;
	int n = msys->n;
	int number_active_links = 0;

        for(i = 0; i < n; i++)
	{
		for(j = 0; j < n; j++)
		{
			if(active_condition(msys, i, j, delta))
				number_active_links++;
		}
	}
	return number_active_links;
}


int active_links(mysys *msys, double delta, link *list_active_links)
{
	int i, j, k;
	int n = msys->n;

	k = 0;	
        for(i = 0; i < n; i++)
	{
		for(j = 0; j < n; j++)
		{
			if(active_condition(msys, i, j, delta))
			{
				list_active_links[k].i = i;
				list_active_links[k].j = j;
				k++;
			}
		}
	}
		
	return 1;
}
