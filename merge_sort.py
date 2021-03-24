"""
Provide implementation for Merge Sort
a. Work on your own comments to explain the code.
b. Provide a different drive code to test those.
c. Use python to demonstrate the execution time of your code.
"""

import time

# start the time counter
start = time.time()


# This function will first divide the array in halves then merge the arrays in order
def merge_sort(arr):
    # First part
    # first it will check if the length of the array is bigger than 1 (to see if there is more than 1 element)
    if len(arr) > 1:
        # if it is bigger, find the middle element, by getting the length and dividing by 2
        mid = len(arr)//2
        # separate the arrays in left and right - first and second halves
        L = arr[:mid]
        R = arr[mid:]
        # print(L, R)
        # call the function until the length is 1
        merge_sort(L)
        merge_sort(R)

        # Second part:
        # Assigning a variable 0 which will be the index for all the arrays
        i = 0
        j = 0
        k = 0

        # while the index is smaller than the length of the arrays, keep running the code below
        # this is just to check if we are interacting with all the elements in the array
        while i < len(L) and j < len(R):
            # compare the two smallest elements, one from each array,
            # and assigning the smaller one into the original array
            # in the correct index
            # if the smallest element in the L array is smaller than the one in the R array
            if L[i] < R[j]:
                # assign the value as the element in the correspondent index in the original array
                arr[k] = L[i]
                # increase the index by 1 of the L array
                i += 1
            else:
                # if the element is greater than the element in the R then assign
                # the value to element in index k
                arr[k] = R[j]
                # increase the index by 1 of the R array
                j += 1
            # after assigning a value in the correct index in the original array
            # increase the index by one to find the next smaller element
            k += 1

        # after comparing the elements, check if there is any element left in L
        # and if there is, include it in the sorted array
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # do the same for R, check if there is any element left
        # and if there is, include it in the sorted array
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 5, 0, 15, 124, 54, 2, 3, 4, 5]
    print("Given array is: ", arr)
    merge_sort(arr)
    print("Sorted array is: ", arr)

# end the time counter and print the running time
end = time.time()
print(f"This program runtime is {end - start}.")