'''
Given an array arr[] of N non-negative integers representing the height of blocks.
If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.

 Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output:
10

Complete Solution:
We need to store water.

But water can only be stored if the right wall and left wall are taller than the centre wall.

We can do this by computing 2 arrays, one for all the right walls, and another for all the left walls.



1. Build the right and left max arrays.
2. Traversing from start, take the minimum of both these maximum arrays,
and subtract  the value of current index in original array, and store this value.
Think about it. The water stored is restricted by both side, and the
 height of water stored will be equal to the height of lower side which could be left or right.

The  answer is summation of all values stored.

'''
def findWater(arr,n):

    #Intialization
    left =[0]*n
    right=[0]*n

    water=0

    #Computiong and looping
    left[0]=arr[0]
    for i in range(1,n):
        left[i]=max(left[i-1], arr[i])

    right[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        right[i] = max(right[i+1], arr[i])

    for i in range(0,n):
        water+=min(left[i],right[i]) - arr[i]

    return water

print(findWater([3,0,0,2,0,4],6))










