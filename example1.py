import time

start_time = time.time()

total = 0
for i in range(1, 10000):
    for j in range(1, 10000):
        total += i + j

print(f"The result is {total}")

end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")

'''
python3 example1.py
pypy3 example1.py

Installation: 
wget https://downloads.python.org/pypy/pypy3.9-v7.3.11-linux64.tar.bz2
tar xf pypy3.9-v7.3.11-linux64.tar.bz2
./pypy3.9-v7.3.11-linux64/bin/pypy3 example1.py
'''