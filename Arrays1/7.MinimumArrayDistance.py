# # You are given an array A, of N elements.
# Find minimum index based distance between two elements of the array, x and y.
# Input:
# N = 4
# A[] = {1,2,3,2}
# x = 1, y = 2
# Output: 1
# Explanation: x = 1 and y = 2. There are
# two distances between x and y, which are
# 1 and 3 out of which the least is 1.

def minDistance(arr, n, x, y):
    recent_x, recent_y = -1, -1
    ans = 9999999

    for i in range(n):
        if arr[i] == x:
            recent_x = i
            if recent_y != -1:
                ans = min(ans, abs(recent_x - recent_y))
        elif arr[i] == y:
            recent_y = i
            if recent_x != -1:
                ans = min(ans, abs(recent_x - recent_y))

    if ans == 9999999:
        return -1
    return ans


print(minDistance([1, 3, 2, 4, 5, 2, 5], 7, 1, 2))
