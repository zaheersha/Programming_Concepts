'''
Given an array arr of size n and an integer X. Find if there's a triplet in
the array which sums up to the given integer X.


Example 1:

Input:
n = 6, X = 13
arr[] = [1 4 45 6 10 8]
Output:
1
Explanation:
The triplet {1, 4, 8} in
the array sums up to 13.

Sort the given array.
Loop over the array and fix the first element of the possible triplet, arr[i].
Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum,
If the sum is smaller than the required number, increment the first pointer.
Else, If the sum is bigger, decrease the end pointer to reduce the sum.
Else, if the sum of elements at two-pointer is equal to given number return true.
'''


def find3Numbers(A, n, X):
    A.sort()

    for i in range(n - 2):
        l = i + 1
        r = n - 1

        while (l < r):
            curr_sum = A[i] + A[l] + A[r]
            if curr_sum == X:
                arrList = [A[i], A[l], A[r]]
                return arrList

            elif curr_sum < X:
                l += 1
            else:
                r -= 1
    return "No Triplets for that number"


print(find3Numbers([1, 4, 45, 6, 10, 8], 6, 13))
