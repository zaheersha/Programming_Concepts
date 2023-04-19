# Given an array nums[] of size n, construct a Product Array P (of same size n) such
# that P[i] is equal to the product of all the elements of nums except nums[i].
#
# Input:
# n = 5
# nums[] = {10, 3, 5, 6, 2}
# Output:
# 180 600 360 300 900
# Explanation:
# For i=0, P[i] = 3*5*6*2 = 180.
# For i=1, P[i] = 10*5*6*2 = 600.
# For i=2, P[i] = 10*3*6*2 = 360.
# For i=3, P[i] = 10*3*5*2 = 300.
# For i=4, P[i] = 10*3*5*6 = 900.

# Compute product of all elements of array in from left and right in
# left(let) and right(let) array.Then start traversing from i = 0.
# For every element the answer will left(i-1) * right(i+1).
# Handle corner cases for first and last element.

def productExceptSelf(arr, n):
    if n==1:
        return [1]

    i, temp=1, 1

    prod = [1 for i in range(n)]

    #left side
    for i in range(n):
        prod[i] = temp
        temp *=arr[i]

    temp =1
    #right
    for i in range (n-1, -1, -1):
        prod[i]*=temp
        temp*=arr[i]

    for i in range(n):
        print(prod[i], end=" ")

    return prod

productExceptSelf([10,3,5,6,2],5)


