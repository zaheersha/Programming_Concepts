# You are given an array arr[] of N integers including 0.
# The task is to find the smallest positive number missing from the array.
#
# Example 1:
#
# Input:
# N = 5
# arr[] = {1,2,3,4,5}
# Output: 6
# Explanation: Smallest positive missing
# number is 6.

#Function that returns the smallest possible number from
#an array of positive numbers

def findMissingPositiove(arr, n):
    for i in range(n):
        if abs(arr[i]) -1 < n and arr[abs(arr[i]) -1] > 0:
            arr[abs(arr[i]) -1] = -arr[abs(arr[i]) -1]

    for i in range(n):
        if(arr[i] > 0):
            return i+1
    return n+1



#Function that puts all non-positive numbers on the left side
#if the array. 0 and negative

def segregate(arr, n):
    j = 0
    for i in range(n):
        if(arr[i] <= 0):
            arr[i], arr[j] = arr[j], arr[i]
            j+=1
    return j

#Create the driver function

def missingNumber(arr, n):

    shift = segregate(arr, n)
    return findMissingPositiove(arr[shift:], n - shift)


print(missingNumber([1,2,3,-4,5,6], 6))







