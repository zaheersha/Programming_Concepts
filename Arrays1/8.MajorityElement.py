# Given an array A of N elements. Find the majority element in the array.
# A majority element in an array A of size N is an element that appears more than N/2 times in the array.
# #Input:
# N = 5
# A[] = {3,1,4,3,2}
# Output:
# 3
# Explanation:
# Since, 3 is present more
# than N/2 times, so it is
# the majority element.

#1. Traverse the array to find the maximum element
#2. Check if that element appears more than N/2 times.


def findCandidate(A):
    #initialization
    maj_index = 0
    count =1
    for i in range(len(A)):
        if A[maj_index] == A[i]:
            count+=1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index] # 1, 2, 1, 1


def isMajority(A, cand):
    count =0
    for i in range(len(A)):
        if A[i] ==cand:
            count+=1
    if count > len(A)/2:
        return True
    else:
        return False

def majorityElement(A, N):
    cand = findCandidate(A)

    if isMajority(A, cand) == True:
        return cand
    else:
        return -1


print(majorityElement([5,1,5,5,2],5))
