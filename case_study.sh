N=$1
NO_OF_ITER=$2

gcc -O3 case_study/MatrixMultiplication.c -o MatrixMultiplication
./MatrixMultiplication ${N} ${NO_OF_ITER} > case_study/results/c.txt

javac case_study/MatrixMultiplication.java 
java case_study/MatrixMultiplication ${N} ${NO_OF_ITER} > case_study/results/java.txt

python3 case_study/MatrixMultiplication.py ${N} ${NO_OF_ITER} > case_study/results/python.txt

python3 case_study/results/findings.py ${N} ${NO_OF_ITER}