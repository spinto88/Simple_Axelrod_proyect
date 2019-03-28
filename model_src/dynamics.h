#ifndef DYNAMICS_H
#define DYNAMICS_H

#include <stdio.h>
#include <stdlib.h>

struct _mysys
{
	int n;
	double **corr;
	int **a;
        int seed;
};
typedef struct _mysys mysys;

int dynamics(mysys *, double, int);

#endif
