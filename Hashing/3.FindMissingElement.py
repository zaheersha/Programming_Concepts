'''
Given two arrays A and B contains integers of size N and M,
the task is to find numbers which are present in the first array, but not present in the second array.

Example 1:

Input: N = 6, M = 5
A[] = {1, 2, 3, 4, 5, 10}
B[] = {2, 3, 1, 0, 5}
Output: 4 10
Explanation: 4 and 10 are present in
first array, but not in second array.
add()
append()
#Array: same type of element, Repeating is possible
#Set: Same type of element, Repeating is prohibited
'''


def findMissing(A, B, N, M):
    s = set()
    ans = []

    for i in B:
        s.add(i)

    for i in A:
        if i not in s:
            ans.append(i)

    return ans


print(findMissing([1, 2, 3, 4, 5, 10], [2, 3, 1, 0, 5], 6, 5))

