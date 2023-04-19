# Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not.
# Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation)
# of elements may be different though.
# Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
#
# Example 1:
#
# Input:
# N = 5
# A[] = {1,2,5,4,0}
# B[] = {2,4,5,0,1}
# Output: 1
# Explanation: Both the array can be
# rearranged to {0,1,2,4,5}

'''

Algorithm:

Use a map or HashMap to store the frequency of elements.
Increment frequencies of elements present in first array.
Decrement frequencies of elements present in second array.
Iterate over the map.
If frequency of any element now is not zero it means that its count in two arrays was not equal.
Return true or false.
'''


def check(A,B,N):

    mp = {}

    for i in range(N):
        if A[i] in mp.keys():
            mp[A[i]] += 1
        else:
            mp[A[i]] = 1

    for i in range(N):
        if B[i] not in mp.keys():
            return False
        mp[B[i]] -= 1

    for i in mp.keys():
        if mp[i] != 0:
            return False

    return True

print(check([1,2,5,4,0], [2,4,5,0,1],5))





