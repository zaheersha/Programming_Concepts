'''
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input:
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated
into ascending order.
'''


#
# These are the folowing steps:
#
# Maintain 3 variables low, high and mid
# low - all elements before low are 0
# mid - all elements between low and mid are 1
# high - all elements after high are 2
# Initially low, mid are set at 0 and high is at n-1
# Now, we iterate mid from 0 to high, and for every element
# if it is equal to 0, we swap it with element at low, and increement low and mid
# else if it is equal to 2, we swap it with element at high, and decreement high
# else we just increement mid (i.e element is equla to 1)
# This method ensures partition, as low and high maintain elements according
# to their values, and then change their positions, ensuring all elements before
# low are lower than low_value and all elements after high are higher than high_value


def sort012(A, N):
    # Init
    low = 0
    high = N - 1
    mid = 0

    while mid <= high:
        if A[mid] == 0:
            A[mid], A[low] = A[low], A[mid]
            mid += 1
            low += 1
        elif A[mid] == 1:
            mid += 1
        else:
            A[mid], A[high] = A[high], A[mid]
            high -= 1

    return A


print(sort012([0, 2, 1, 2, 0], 5))
