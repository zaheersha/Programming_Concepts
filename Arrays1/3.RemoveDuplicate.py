# Given a sorted array A[] of size N show how many unduplicated elements there are
# Note: Don't use set or HashMap to solve the problem.
#
# Input:
# N = 5
# Array = {2, 2, 2, 3, 3}
# Output: 2
# Explanation: After removing all the duplicates
# only one instance of 2 will remain.

def removeDuplicate(A,N):
    i=0
    for j in range(1,N):
        if A[i] != A[j]:
            i+=1
            A[i]=A[j]
    return (i+1)

print(removeDuplicate([2,2,2,3,3,4,4,5],8))






































