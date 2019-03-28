#include "dynamics.h"

int dynamics(mysys *msys, double delta, int steps)
{
	int i, j, k;
	double random;
	int step = 0;
	int step_n = 0;
	double aux = 0.00;
	int n = msys->n;
	double factor;

	while(step < steps)
	{
		step_n = 0;
	        srand(msys->seed);
		while(step_n < n)
		{
			i = rand() % n;
			j = rand() % n;
			while(msys->a[i][j] == 0)
				j = (j+1) % n;

			random = (double)rand()/RAND_MAX;

		        if((random < msys->corr[i][j]) && (msys->corr[i][j] > (delta * 0.5)))
			{		
				aux = msys->corr[i][j] + delta;
				if(aux >= 1.00)
					aux = 1.00;	
				if(aux < 1.00)
				{
				        factor = 1.00 / (1.00 - msys->corr[i][j]);
					for(k = 0; k < n; k++)
					{
						if((k!=i) && (k!=j))
						{
							msys->corr[i][k] += (msys->corr[j][k] - msys->corr[i][k]) * factor * delta;
							msys->corr[k][i] = msys->corr[i][k];
						}
					}
				}	
				else if(aux == 1.00)
				{
					for(k = 0; k < n; k++)
					{
						if((k!=i) && (k!=j))
						{
							msys->corr[i][k] = msys->corr[j][k];	
							msys->corr[k][i] = msys->corr[i][k];	
						}
					}
				}
				msys->corr[i][j] = aux;
				msys->corr[j][i] = msys->corr[i][j];
			}
			step_n++;
		}
		step++;
	        msys->seed = rand();
	}

	return 1;
}
