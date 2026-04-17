#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>

// This is a comment.

/*
This is a multi-line comment.
*/

//Like Java, you must have a main method.
int main(int argc, char **argv) {

    // Like Java, you must declare variable types and use semicolons.
    uint8_t i = 10;
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
    int *arr = malloc(sizeof(int)*2);
    *arr = 0;
    arr += 1;
    *arr = 1;

    //Of course, you can always use brackets for array accesses
    printf("%d", arr[0]);

    //We can also have pointers to pointers, so here's a 2D array for example:
    int **matrix = malloc(sizeof(int*)*5);
    for (int i = 0; i < 5; i++) {
        *(matrix + i) = malloc(5*sizeof(int));
    }
    //Setting row 2, col 2 to 5
    *(*(matrix + 2)+2) = 5;

    //When done, be sure to free unused memory locations.
    //You MUST free the original malloc location.
    
    free(arr-1);
    
    for (int i = 0; i< 5; i++) {
        free(*(matrix + i));
    }
    free(matrix);

    return EXIT_SUCCESS;
}


