from sorting.algorithms.sorts import *
from sorting.utils.util import *
import random
from time import time 
# from uniplot import plot
  
def timer_func(func): 
    def wrap_func(*args, **kwargs): 
        t1 = time() 
        result = func(*args, **kwargs) 
        t2 = time() 
        print(f"  {(t2-t1):>08.4f} seconds - {func.__name__!r}") 
        return result 
    return wrap_func 
  
SIZE = 20_000

@timer_func
def generate_ascending_list(size: int) -> list:
    return list(range(1,SIZE+1,1))

@timer_func
def generate_descending_list(size: int) -> list:
    return list(range(SIZE,0,-1))

@timer_func
def generate_random_list(size: int) -> list:
    return random.sample(range(1, SIZE+1), SIZE)

print(f"Generating {SIZE} numbers in ascending, descending, and random order")
data_sorted_ascending = generate_ascending_list(SIZE)
data_sorted_descending = generate_descending_list(SIZE)
data_sorted_randomly = generate_random_list(SIZE)

# show_list(size = SIZE, title = "ascending", data = data_sorted_ascending)
# print()
# show_list(size = SIZE, title = "descending", data = data_sorted_descending)
# print()
# show_list(size = SIZE, title = "random", data = data_sorted_randomly)

# Here are some of the most common sorting algorithms:
# 
# 1. **Selection Sort**: This algorithm sorts an array by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning. It has a time complexity of **O(n^2)** ¹.
# 
# 2. **Bubble Sort**: This algorithm repeatedly swaps adjacent elements if they are in the wrong order. It has a time complexity of **O(n^2)** ².
# 
# 3. **Insertion Sort**: This algorithm builds the final sorted array one item at a time. It has a time complexity of **O(n^2)** ¹.
# 
# 4. **Merge Sort**: This algorithm divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. It has a time complexity of **O(n log n)** ¹².
# 
# 5. **Quick Sort**: This algorithm picks an element as a pivot and partitions the given array around the picked pivot. It has a time complexity of **O(n log n)** ¹.
# 
# 6. **Heap Sort**: This algorithm sorts an array by first building a heap from the input array and then repeatedly removing the largest element from the heap and adding it to the end of the sorted array. It has a time complexity of **O(n log n)** ¹.
# 
# 7. **Counting Sort**: This algorithm sorts an array by counting the number of occurrences of each unique element in the array and then using arithmetic to calculate the position of each element in the sorted output array. It has a time complexity of **O(n + k)**, where k is the range of the non-negative key values ¹.
# 
# 8. **Radix Sort**: This algorithm sorts an array by grouping the individual digits of the same place value. It has a time complexity of **O(nk)**, where k is the number of digits in the longest number ¹.
# 
# 9. **Bucket Sort**: This algorithm sorts an array by distributing the elements of the array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sorting algorithm. It has a time complexity of **O(n + k)** ¹.


print("\nSorting data sorted ascending...")
(bubble_time_in_seconds, _) = bubble(data_sorted_ascending)
(counting_time_in_seconds, _) = counting(data_sorted_ascending)
(heap_time_in_seconds, _) = heap(data_sorted_ascending)
(insertion_time_in_seconds, _) = insertion(data_sorted_ascending)
(merge_time_in_seconds, _) = merge(data_sorted_ascending)
# quick(data_sorted_ascending)
(selection_time_in_seconds, _) = selection(data_sorted_ascending)
(shell_time_in_seconds, _) = shell(data_sorted_ascending)

sort_names = ["Bubble", "Counting", "Heap", "Insertion", "Merge", "Selection", "Shell"]
sort_times = [bubble_time_in_seconds, counting_time_in_seconds, heap_time_in_seconds, insertion_time_in_seconds, merge_time_in_seconds, selection_time_in_seconds, shell_time_in_seconds]
new_list = [round(t,4) for t in sort_times]
show_list(size = SIZE, labels = sort_names, data = new_list, title = "ascending")

print("\nSorting data sorted descending...")
(bubble_time_in_seconds, _) = bubble(data_sorted_descending)
(counting_time_in_seconds, _) = counting(data_sorted_descending)
(heap_time_in_seconds, _) = heap(data_sorted_descending)
(insertion_time_in_seconds, _) = insertion(data_sorted_descending)
(merge_time_in_seconds, _) = merge(data_sorted_descending)
# quick(data_sorted_descending)
(selection_time_in_seconds, _) = selection(data_sorted_descending)
(shell_time_in_seconds, _) = shell(data_sorted_descending)

sort_times = [bubble_time_in_seconds, counting_time_in_seconds, heap_time_in_seconds, insertion_time_in_seconds, merge_time_in_seconds, selection_time_in_seconds, shell_time_in_seconds]
new_list = [round(t,4) for t in sort_times]
show_list(size = SIZE, labels = sort_names, data = new_list, title = "descending")

print("\nSorting data sorted randomly...")
(bubble_time_in_seconds, _) = bubble(data_sorted_randomly)
(counting_time_in_seconds, _) = counting(data_sorted_randomly)
(heap_time_in_seconds, _) = heap(data_sorted_randomly)
(insertion_time_in_seconds, _) = insertion(data_sorted_randomly)
(merge_time_in_seconds, _) = merge(data_sorted_randomly)
# quick(data_sorted_descending)
(selection_time_in_seconds, _) = selection(data_sorted_randomly)
(shell_time_in_seconds, _) = shell(data_sorted_randomly)

sort_times = [bubble_time_in_seconds, counting_time_in_seconds, heap_time_in_seconds, insertion_time_in_seconds, merge_time_in_seconds, selection_time_in_seconds, shell_time_in_seconds]
new_list = [round(t,4) for t in sort_times]
show_list(size = SIZE, labels = sort_names, data = new_list, title = "randomly")
