# Given an unsorted array arr[] of size N, rotate it by D elements (clockwise).
#
# Input:
#  N denoting the size
# of the array and an integer D denoting the number size of the rotation. Subsequent
# line will be the N space separated array elements.

# Output:
# For each testcase, in a new line, output the rotated array.
#
# Constraints:
# 1 <= N <= 107
# 1 <= D <= N
# 0 <= arr[i] <= 105

#Example:
#5
#2
#1 2 3 4 5


#We will use reversed

def rotateArray(d, n, list):
    list[0:d] = reversed(list[0:d])
    #2 1 3 4 5
    list[d:n] = reversed(list[d:n])
    #2 1 5 4 3
    list[0:n] = reversed(list[0:n])
    #3 4 5 1 2

if __name__ =="__main__":
    n = int(input())
    d = int(input())
    list = [int(x) for x in input().strip().split()]

    rotateArray(d, n, list)

    for i in range(n):
        print(list[i], end=" ")
    print()



