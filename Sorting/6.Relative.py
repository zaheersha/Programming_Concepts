'''
Given two integer arrays A1[ ] and A2[ ] of size N and M respectively. Sort the first array A1[ ]
such that all the relative positions of the elements in the first array are the same as the elements in the second array A2[ ].
See example for better understanding.
Note: If elements are repeated in the second array, consider their first occurance only.

Example 1:

Input:
N = 11
M = 4
A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
A2[] = {2, 1, 8, 3}
Output:
2 2 1 1 8 8 3 5 6 7 9
Explanation: Array elements of A1[] are
sorted according to A2[]. So 2 comes first
then 1 comes, then comes 8, then finally 3
comes, now we append remaining elements in
sorted order.


Algorithm:

Store all the elements of first array in map.
Traverse over the second array and store all those elements which are present in map.
Iterate over the map and store the rest elements present in map.

'''


def relativeSort(A1, N, A2, M):
    d = {};
    for i in A1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    ans = []
    an = []

    arr = set(A1) - set(A2)

    for i in arr:
        if i in d:
            an.extend([i] * d[i])

    for i in A2:
        if i in d:
            ans.extend([i] * d[i])

    ll = list(an)
    ll.sort()

    ans.extend(ll)

    return ans


print(relativeSort([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8], 11, [2, 1, 8, 3], 4))
