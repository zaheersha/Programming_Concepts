'''
Given two strings A and B, find if A is a subsequence of B.

Input:
A = prgai
B = ilikeprogramming
Output: 1
Explanation: A is a subsequence of B.

Maintain 2 pointers, one in string A and the other in string B.
Traverse both the string together. If character in A matches character
in B, increment both pointer. Otherwise increment pointer in string B only.

'''

def isSubSequence(A,B):
    i=j=0

    while i < len(B) and j < len(A):
        if A[j] == B[i]:
            j+=1
            i=0
        i+=1

    return j == len(A)

print(isSubSequence("prgail","ilikeprogramming"))


