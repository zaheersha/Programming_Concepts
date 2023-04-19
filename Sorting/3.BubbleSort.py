# Given an Integer N and a list arr. Sort the array using bubble sort algorithm.
# Example 1:
#
# Input:
# N = 5
# arr[] = {4, 1, 3, 9, 7}
# Output:
# 1 3 4 7 9
#
# To sort an array in increasing order in Bubble Sort, we move the greatest element at the
# end in first pass.  To do this we compare adjacent elements.
#
# In one pass, we compare every element to its next.  If next element is smaller,
# we swap them else we do nothing.

def bubbleSort(arr, n):

    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


print(bubbleSort([4, 1, 3, 9, 7], 5))


