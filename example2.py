import time


# Bad: 447ms
start_time = time.time()

nums_sum_list_comprehension = sum([num**2 for num in range(1000000)])

end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")




# Good: 300ms
start_time = time.time()

nums_sum_generator_expression = sum((num**2 for num in range(1000000)))

end_time = time.time()
print(f"It took {end_time-start_time} seconds to compute")

# Bonus

import sys
# Bad
nums_squared_list = [num**2 for num in range(1000000)]
print(sys.getsizeof(nums_squared_list))  # 87632
# Good
nums_squared_generator = (num**2 for num in range(1000000))
print(sys.getsizeof(nums_squared_generator))  # 128
