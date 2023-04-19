'''
Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m.
Task is to check whether a2[] is a subset of a1[] or not.
Both the arrays can be sorted or unsorted. It may be assumed that elements in both array are distinct.


Example 1:

Input:
a1[] = {11, 1, 13, 21, 3, 7}
a2[] = {11, 3, 7, 1}
Output:
Yes
Explanation:
a2[] is a subset of a1[]

Create a Hash Table for all the elements of arr1[].
Traverse arr2[] and search for each element of arr2[] in the Hash Table.
If element is not found then return 0.
If all elements are found then return 1.

'''


def isSubset(a1, a2):
    s = set()
    for i in range(len(a1)):
        s.add(a1[i])

    p = len(s)
    for i in range(len(a2)):
        s.add(a2[i])
    if len(s) == p:
        return "Yes"
    return "No"


print(isSubset([11, 1, 13, 21, 3, 7], [33 ,11, 3, 7, 1]))
