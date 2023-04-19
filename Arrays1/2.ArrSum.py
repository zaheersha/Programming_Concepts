# Given an integer array arr of size n, you need to sum the elements of arr.
# Input:
# n = 3
# arr[] = {3 2 1}
# Output: 6

def sumElements(arr, n):
    sm=0

    for e in arr:
        sm+=e
    return sm

print(sumElements([4,3,7,1],4))



















