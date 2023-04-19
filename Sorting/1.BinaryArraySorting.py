# Given a binary array A[] of size N.The task is to arrange the
# array in increasing order. Note: The binary array contains only 0 and 1.
#
# Input:
# 5
# 1 0 1 1 0
#
# Output:
# 0 0 1 1 1
#Algorithm
# Segregated approach
# Run a loop till left index is smaller than or equal to right index.
# For every iteration:
# If element at left index is 0, increase the left index.
# Else If element at high index is 1, decrease the right index.
# Else, swap the elements at left and right index and update the left and right index.
#
#

def binSort(A, N):

    #initialization
    left = 0
    right = N-1

    #Segregation method
    while left < right:

        while A[left] == 0 and left < right:
            left += 1

        while A[right] == 1 and left < right:
            right -= 1

        #left < right == there is 1 at left and 0 at right

        if left < right:
            A[left] = 0
            A[right] = 1
            left += 1
            right -=1

        return A

print(binSort([1, 0, 1, 1, 0], 5))













