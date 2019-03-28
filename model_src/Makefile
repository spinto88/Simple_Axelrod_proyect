
all:
	gcc -c -fPIC -O3 -Wall -g dynamics.c -o dynamics.o 
	gcc -shared dynamics.o -o libc.so
clean:
	rm -rfv dynamics.o libc.so *.pyc
