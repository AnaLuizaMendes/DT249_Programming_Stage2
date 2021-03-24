"""
Provide implementation for Quick Sort
a. Work on your own comments to explain the code.
b. Provide a different drive code to test those.
c. Use python to demonstrate the execution time of your code.
"""

import time
import random

# start the time counter
start = time.time()


# this function will implement quicksort, the arr is the array, first is the first element index, and
# last is the last element index
def quicksort(arr, first, last):
    # check if the array has more than one element
    if first < last:
        # call the functions to select the pivot and sort the sub-arrays (less than and greater than the pivot)
        pivot_i = select_pivot(arr, first, last)
        quicksort(arr, first, pivot_i - 1)
        quicksort(arr, pivot_i + 1, last)

# function to find the pivot, and replace it with the first element in the array
def select_pivot(arr, first, last):
    # find randomly one element between the first and last element of the array, and assign this element as the pivot
    pivot = random.randrange(first, last)
    # after finding the pivot, we need to change it to a known index, in this case first index of the array
    # swap the pivot with the first element
    arr[first], arr[pivot] = arr[pivot], arr[first]
    # return the array, and the first and last element (the first element is now the pivot)
    return partition(arr, first, last)


def partition(arr, first, last):
    # pivot is the first element in the array
    pivot = first
    # we will start the interaction on the array from the element after the pivot
    i = first + 1

    # for each element in the array, starting after the pivot index, check if element is less than the pivot
    # if it is, move it to the index i of the array
    for j in range(first + 1, last + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            # increase the index
            i += 1
    # place the pivot after the last of the smaller than the pivot elements
    #  this will be the pivot the correct index for the final order
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return (pivot)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 5, 0, 15, 124, 54, 2, 3, 4, 5]
    print("Given array is: ", arr)
    quicksort(arr, 0, len(arr) - 1)
    print("Sorted array is: ", arr)

# end the time counter and print the running time
end = time.time()
print("This program runtime is {}".format(end - start))