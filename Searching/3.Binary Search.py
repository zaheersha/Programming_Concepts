# Given a sorted array of size N and an integer K,
# find the position at which K is present in the array using binary search.
#
#
# Example 1:
#
# Input:
# N = 5
# arr[] = {1 2 3 4 5}
# K = 4
# Output: 3
# Explanation: 4 appears at index 3.

#Binary Search Function
def binarySearch(arr, left, right, key):
    if left > right:
        return -1
    mid = (left + right)//2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binarySearch(arr, left, mid - 1, key)
    else:
        return binarySearch(arr, mid + 1, right, key)


#Driver function

def driver(arr, n, k):
    return binarySearch(arr, 0, n-1, k)

print(driver([1,2,3,4,5], 5, 4))