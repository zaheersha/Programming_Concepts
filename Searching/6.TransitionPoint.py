# Given a sorted array containing only 0s and 1s, find the transition point.
#
#
# Example 1:
#
# Input:
# N = 5
# arr[] = {0,0,0,1,1}
# Output: 3
# Explanation: index 3 is the transition
# point where 1 begins.

#The last element that is equal to 0

def transitionPoint(arr, n):
    #Base case
    if arr[0]==1:
        return 0

    #Initialization
    start = 0
    end = n-1

    while (start <= end):

        #Find the middle
        mid = (int)((start + end)//2)

        if (arr[mid] == 0):
            start = mid +1
        elif (arr[mid] == 1):
            if (arr[mid-1] == 0):
                return mid
            end = mid-1
    return -1


print(transitionPoint([0,0,0,0,1,1], 6))





