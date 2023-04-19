# Given an array A of positive integers. Your task is to find
# the leaders in the array. An element of array is leader if it is
# greater than or equal to all the elements to its right side. The rightmost element is always a leader.

# Input:
# n = 6
# A[] = {16,17,4,3,5,2}
# Output: 17 5 2
# Explanation: The first leader is 17
# as it is greater than all the elements
# to its right.  Similarly, the next
# leader is 5. The right most element
# is always a leader so it is also
# included.

# 1.Start iterating from the last element.
#
# 2.Check whether the current element is greater than the maximum stored till now
#
# 3.If it is greater, store the current element in a list and then update the maximum.
#
# 4.Reverse the list and return it.

def leaders(A, N):
    ans=[]
    maxx=A[N-1]

    for i in range(N-1, -1, -1):
        if A[i]>=maxx:
            maxx=A[i]
            ans.append(maxx)

    ans.reverse()
    return ans

print(leaders([1,2,3,4,0], 5))