#include <stdlib.h>
#include <stdio.h>
#include <time.h>


int main(int argc, char **argv) {
    if(argc < 3) {
        printf("Provide n and no_of_iter\n");
        exit(1);
    }
    
    int no_of_iter = atoi(argv[2]);
    int n = atoi(argv[1]);

    double **A,**B,**C;

    A = (double**)malloc(sizeof(double*)*n);
    for (int i = 0; i < n; i++)
        A[i] = (double*)malloc(sizeof(double)*n);

    B = (double**)malloc(sizeof(double*)*n);
    for (int i = 0; i < n; i++)
        B[i] = (double*)malloc(sizeof(double)*n);
    
    C = (double**)malloc(sizeof(double*)*n);
    for (int i = 0; i < n; i++)
        C[i] = (double*)malloc(sizeof(double)*n);

        
    // populate the matrices with random values between 0.0 and 1.0
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {

            A[i][j] = (double) rand() / (double) RAND_MAX;
            B[i][j] = (double) rand() / (double) RAND_MAX;
            C[i][j] = 0;
        }
    }

    // Display
    // for (int i = 0; i < n; i++) {
    //     for (int j = 0; j < n; j++) {

    //         printf("%f ", A[i][j]);
    //         // printf("%f ", B[i][j]);
    //         // printf("%f ", C[i][j]);
    //     }
    //     printf("\n");
    // }

    for (int p=0; p<no_of_iter; p++) {
        struct timespec start, end;
        double time_spent;

        //matrix multiplication
        clock_gettime(CLOCK_REALTIME, &start);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        clock_gettime(CLOCK_REALTIME, &end);
        time_spent = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1000000000.0;
        printf("%.2f\n", time_spent);

    }

    return 0;
}