import time

# Bad: 5.95s
def computeSum1(size: float) -> int:
    sum = 0
    for i in range(size):
        sum += i
    return sum

def main1():
    size = 10000
    for _ in range(size):
        sum = computeSum1(size)

start_time = time.time()
main1()
end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")


# Good: 2.27s
# pip3 install numba
import numba

@numba.jit
def computeSum2(size: float) -> int:
    sum = 0
    for i in range(size):
        sum += i
    return sum

def main2():
    size = 10000
    for _ in range(size):
        sum = computeSum2(size)

start_time = time.time()
main2()
end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")