#include "active_links.h"

int active_links(mysys *msys, double delta)
{
	int i, j;
	int n = msys->n;

        for(i = 0; i < n; i++)
	{
		for(j = (i+1); j < n; j++)
		{
			if((msys->a[i][j] == 1) && (msys->corr[i][j] < 1.00) && (msys->corr[i][j] > (delta * 0.5)))
				return 1;
		}
	}	
	return 0;
}
