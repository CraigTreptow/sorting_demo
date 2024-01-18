import asciibars
import random
from sorting.algorithms.sorts import *

def generate_ascending_list(size: int) -> list:
    return list(range(1,size+1,1))

def generate_descending_list(size: int) -> list:
    return list(range(size,0,-1))

def generate_random_list(size: int) -> list:
    return random.sample(range(1, size+1), size)

def run_sorts(data: list, size: int, label: str) -> None:
    print(f"\nSorting {label} data...", end="")
    (bubble_time_in_seconds, _) = bubble(data)
    (counting_time_in_seconds, _) = counting(data)
    (heap_time_in_seconds, _) = heap(data)
    (insertion_time_in_seconds, _) = insertion(data)
    (merge_time_in_seconds, _) = merge(data)
    (selection_time_in_seconds, _) = selection(data)
    (shell_time_in_seconds, _) = shell(data)
    print("done.\n")

    sort_names = ["Bubble", "Counting", "Heap", "Insertion", "Merge", "Selection", "Shell"]
    sort_times = [bubble_time_in_seconds, counting_time_in_seconds, heap_time_in_seconds, insertion_time_in_seconds,
                  merge_time_in_seconds, selection_time_in_seconds, shell_time_in_seconds]
    new_list = [round(t,4) for t in sort_times]
    show_list(size = size, labels = sort_names, data = new_list, title = label)

def show_list(data: list, size: int, labels: list = [], title: str = "Values (larger are taller)") -> None:
    """
    Shows a list horizontally, with vertical bars corresponding to the size of the number.
    """

    if labels:
        data = list(zip(labels, data))
    else:
        generated_labels = map(str, list(range(1, size+1, 1)))
        data = list(zip(generated_labels, data))

    print(f"{title.capitalize()}\n")
    # data = list(zip(labels, data))
    asciibars.plot(data)