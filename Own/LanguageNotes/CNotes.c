#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// This is a comment.

/*
This is a multi-line comment.
*/

//Like Java, you must have a main method.
void main(void) {

    // Like Java, you must declare variable types and use semicolons.
    int i = 10;
    char *last = "Hello World!";

    //Unlike Java, Strings don't really "exist" in C, you are forced to use char pointers.
    printf("I am going to say %s\n", last);

    /*
    %d - int
    %f - float
    %lf - double (long float)

    %c - char
    %s - string
    %p - pointer
    */

    //On the topic of pointers, think of them as pretty much the same as arrays in Java.
    int *arr = malloc(sizeof(int));
    *arr = 0;
    arr += 4;
    *arr = 1;

    //We can also have pointers to pointers, so here's a 2D array for example:
    int **matrix = malloc(sizeof(int));
    **matrix = 0;
    *matrix += 4;
    **matrix = 1;
    *matrix -= 4;
    matrix += 4;
    **matrix = 1;

    

}


