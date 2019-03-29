#include "dynamics.h"

int random_neighbour(mysys *msys, int node)
{
	int j, k;
	int random_neigh;
	int node_degree = 0;
	int *neighbors;

        for(j = 0; j < msys->n; j++)
	{
		if(msys->a[node][j] == 1)
			node_degree++;
	}

	neighbors = (int *)malloc(sizeof(int) * node_degree);

        k = 0;
        for(j = 0; j < msys->n; j++)
	{
		if(msys->a[node][j] == 1)
		{
			neighbors[k] = j;
			k++;
		}
	}

	k = rand() % node_degree;
	random_neigh = neighbors[k];

	free(neighbors);

	return random_neigh;
}

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
			j = random_neighbour(msys, i);

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
