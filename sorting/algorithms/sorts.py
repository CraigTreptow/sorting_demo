from time import time 

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


  
def timer_func(func): 
    def wrap_func(*args, **kwargs): 
        t1 = time() 
        result = func(*args, **kwargs) 
        t2 = time() 
        total_time_in_seconds = t2-t1
        # print(f"  {(total_time_in_seconds):>08.4f} seconds - {func.__name__!r}") 
        return (total_time_in_seconds, result)
    return wrap_func 
  
@timer_func
def bubble(data: list) -> list:
    """
    Sorts a list of numbers using the bubble sort algorithm.
    """
    # Iterate through the list
    for i in range(len(data)):
        # Iterate through the list again
        for j in range(len(data)):
            # If the current number is greater than the next number
            if data[i] < data[j]:
                # Swap the numbers
                data[i], data[j] = data[j], data[i]
    # Return the sorted list
    return data

@timer_func
def selection(data: list) -> list:
    """
    Sorts a list of numbers using the selection sort algorithm.
    """
    # Iterate through the list
    for i in range(len(data)):
        # Set the current index as the minimum index
        min_index = i
        # Iterate through the list again
        for j in range(i+1, len(data)):
            # If the current number is less than the minimum number
            if data[j] < data[min_index]:
                # Set the current index as the minimum index
                min_index = j
        # Swap the numbers
        data[i], data[min_index] = data[min_index], data[i]
    # Return the sorted list
    return data

@timer_func
def insertion(data: list) -> list:
    """
    Sorts a list of numbers using the insertion sort algorithm.
    """
    # Iterate through the list
    for i in range(1, len(data)):
        # Set the current number as the key
        key = data[i]
        # Set the current index as the previous index
        j = i - 1
        # While the current index is greater than or equal to zero
        # and the current number is less than the previous number
        while j >= 0 and key < data[j]:
            # Shift the previous number to the right
            data[j+1] = data[j]
            # Decrement the current index
            j -= 1
        # Set the current number as the previous number
        data[j+1] = key
    # Return the sorted list
    return data

@timer_func
def merge(data: list) -> list:
    return do_merge_sort(data)

def do_merge_sort(data: list) -> list:
    """
    Sorts a list of numbers using the merge sort algorithm.
    """
    # If the list has more than one number
    if len(data) > 1:
        # Get the middle index
        mid = len(data) // 2
        # Get the left half of the list
        left = data[:mid]
        # Get the right half of the list
        right = data[mid:]
        # Sort the left half of the list
        do_merge_sort(left)
        # Sort the right half of the list
        do_merge_sort(right)
        # Set the current index as zero
        i = 0
        # Set the left index as zero
        j = 0
        # Set the right index as zero
        k = 0
        # While the left index is less than the length of the left half
        # and the right index is less than the length of the right half
        while j < len(left) and k < len(right):
            # If the current number in the left half is less than the current number in the right half
            if left[j] < right[k]:
                # Set the current number as the current number in the left half
                data[i] = left[j]
                # Increment the left index
                j += 1
            # Otherwise
            else:
                # Set the current number as the current number in the right half
                data[i] = right[k]
                # Increment the right index
                k += 1
            # Increment the current index
            i += 1
        # While the left index is less than the length of the left half
        while j < len(left):
            # Set the current number as the current number in the left half
            data[i] = left[j]
            # Increment the left index
            j += 1
            # Increment the current index
            i += 1
        # While the right index is less than the length of the right half
        while k < len(right):
            # Set the current number as the current number in the right half
            data[i] = right[k]
            # Increment the right index
            k += 1
            # Increment the current index
            i += 1
    # Return the sorted list
    return data

@timer_func
def heap(data: list) -> list:
    """
    Sorts a list of numbers using the heap sort algorithm.
    """
    # Build a max heap
    build_max_heap(data)
    # Iterate through the list in reverse order
    for i in range(len(data)-1, 0, -1):
        # Swap the numbers
        data[0], data[i] = data[i], data[0]
        # Heapify the list
        heapify(data, 0, i)
    # Return the sorted list
    return data

def build_max_heap(data: list) -> list:
    """
    Builds a max heap from a list of numbers.
    """
    # Iterate through the list
    for i in range(len(data)//2, -1, -1):
        # Heapify the list
        heapify(data, i, len(data))
    # Return the heapified list
    return data

def heapify(data: list, i: int, heap_size: int) -> list:
    """
    Heapifies a list of numbers.
    """
    # Set the left index as two times the current index plus one
    left = 2 * i + 1
    # Set the right index as two times the current index plus two
    right = 2 * i + 2
    # Set the largest index as the current index
    largest = i
    # If the left index is less than the heap size
    # and the current number is less than the number at the left index
    if left < heap_size and data[i] < data[left]:
        # Set the largest index as the left index
        largest = left
    # If the right index is less than the heap size
    # and the current number is less than the number at the right index
    if right < heap_size and data[largest] < data[right]:
        # Set the largest index as the right index
        largest = right
    # If the largest index is not the current index
    if largest != i:
        # Swap the numbers
        data[i], data[largest] = data[largest], data[i]
        # Heapify the list
        heapify(data, largest, heap_size)
    # Return the heapified list
    return data

@timer_func
def shell(data: list) -> list:
    """
    Sorts a list of numbers using the shell sort algorithm.
    """
    # Set the gap as half the length of the list
    gap = len(data) // 2
    # While the gap is greater than zero
    while gap > 0:
        # Iterate through the list
        for i in range(gap, len(data)):
            # Set the current number as the key
            key = data[i]
            # Set the current index as the previous index
            j = i
            # While the current index is greater than or equal to the gap
            # and the current number is less than the previous number
            while j >= gap and key < data[j-gap]:
                # Shift the previous number to the right
                data[j] = data[j-gap]
                # Decrement the current index
                j -= gap
            # Set the current number as the previous number
            data[j] = key
        # Set the gap as half the gap
        gap //= 2
    # Return the sorted list
    return data

@timer_func
def counting(data: list) -> list:
    """
    Sorts a list of numbers using the counting sort algorithm.
    """
    # Get the maximum number in the list
    max_num = max(data)
    # Create a list of zeros with a length of the maximum number plus one
    count = [0] * (max_num + 1)
    # Iterate through the list
    for num in data:
        # Increment the current number in the count list
        count[num] += 1
    # Set the current index as zero
    i = 0
    # Iterate through the count list
    for j in range(len(count)):
        # While the current number in the count list is greater than zero
        while count[j] > 0:
            # Set the current number in the list as the current index
            data[i] = j
            # Increment the current index
            i += 1
            # Decrement the current number in the count list
            count[j] -= 1
    # Return the sorted list
    return data
