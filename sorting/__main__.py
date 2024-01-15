from sorting.algorithms.sorts import *
import random
import time

SIZE = 20_000

print(f"Generating {SIZE} numbers in ascending, descending, and random order")

# start_time = time.perf_counter()
data_sorted_ascending = list(range(1,SIZE+1,1))
# end_time = time.perf_counter()

# execution_time = end_time - start_time
# print(f" Generate ascending list: {execution_time:.6f} seconds")

# start_time = time.perf_counter()
data_sorted_descending = list(range(SIZE,0,-1))
# end_time = time.perf_counter()

# execution_time = end_time - start_time
# print(f"Generate descending list: {execution_time:.6f} seconds")

# start_time = time.perf_counter()
data_sorted_randomly = random.sample(range(1, SIZE+1), SIZE)
# end_time = time.perf_counter()

# execution_time = end_time - start_time
# print(f"   Generate random list: {execution_time:.6f} seconds")

print("\nSorting data sorted ascending...")
bubble(data_sorted_ascending)
counting(data_sorted_ascending)
heap(data_sorted_ascending)
insertion(data_sorted_ascending)
# merge(data_sorted_ascending)
# quick(data_sorted_ascending)
selection(data_sorted_ascending)
shell(data_sorted_ascending)
# radix(data_sorted_ascending)

# print(data_sorted_ascending)
# print(data_sorted_descending)
# print(data_sorted_randomly)

# start_time = time.perf_counter()
# bubble(data_sorted_ascending)
# end_time = time.perf_counter()
# 
# execution_time = end_time - start_time
# print(f" Sorted Ascending Execution time: {execution_time:.6f} seconds")
# 
# start_time = time.perf_counter()
# bubble(data_sorted_descending)
# end_time = time.perf_counter()
# 
# execution_time = end_time - start_time
# print(f"Sorted Descending Execution time: {execution_time:.6f} seconds")
# 
# start_time = time.perf_counter()
# bubble(data_sorted_randomly)
# end_time = time.perf_counter()
# 
# execution_time = end_time - start_time
# print(f"  Sorted Randomly Execution time: {execution_time:.6f} seconds")