import cProfile

def computeSum(size: int) -> int:
    return sum(range(size)) 

def main():
    size = 10000
    for _ in range(size):
        sum = computeSum(size)

if __name__ == "__main__":
    cProfile.run("main()")

''' OUTPUT
         20004 function calls in 1.920 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.920    1.920 <string>:1(<module>)
    10000    0.005    0.000    1.917    0.000 example4.py:3(computeSum)
        1    0.003    0.003    1.920    1.920 example4.py:6(main)
        1    0.000    0.000    1.920    1.920 {built-in method builtins.exec}
    10000    1.913    0.000    1.913    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''