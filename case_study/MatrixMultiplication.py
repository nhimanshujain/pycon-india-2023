import random
import time
from sys import argv

if(len(argv)<3):
    print("Provide n and no_of_iter")
    exit(1)

n = int(argv[1])
no_of_iter = int(argv[2])

#populate the matrices with random values between 0.0 and 1.0
A = [[random.random() for row in range(n)] for col in range(n)]
B = [[random.random() for row in range(n)] for col in range(n)]
C = [[0 for row in range(n)] for col in range(n)]


for p in range(no_of_iter):

    start = time.time()
    #matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    end = time.time()
    print("%0.2f" % (end-start))