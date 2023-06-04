import time

start_time = time.time()

c = 0
while True:
    c += 1
    if c > 100000000:
        break
    

end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")



start_time = time.time()

c = 0
while 1:
    c += 1
    if c > 100000000:
        break

end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")