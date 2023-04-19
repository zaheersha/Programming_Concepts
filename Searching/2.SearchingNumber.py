# Given an array Arr of N elements and a integer K. Your task is to return the position
# of first occurence of K in the given array.
# Note: Position of first element is considered as 1.
#
# Example 1:
#
# Input:
# N = 5, K = 16
# Arr[] = {9, 7, 2, 16, 4}
# Output: 4
# Explanation: K = 16 is found in the
# given array at position 4.

def sr(arr, k):
    for i in range(len(arr)):
        if(arr[i] == k):
            return i + 1
    return "The number is not in the Array"


print(sr([9,7,2,16,4],1))



