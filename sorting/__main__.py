from sorting.utils.util import *
from time import time 
import sys

DEFAULT_SIZE = 20_000
  
size = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SIZE

print(f"Generating {size:-6,} numbers in ascending, descending, and random order...", end="")
data_sorted_ascending = generate_ascending_list(size)
data_sorted_descending = generate_descending_list(size)
data_sorted_randomly = generate_random_list(size)
print("done.")

run_sorts(data=data_sorted_ascending, size=size, label="ascending")
run_sorts(data=data_sorted_descending, size=size, label="descending")
run_sorts(data=data_sorted_randomly, size=size, label="random")
