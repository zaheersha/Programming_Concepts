'''
Given an unsorted array Arr of size N of positive integers. One number
'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

Example 1:

Input:
N = 2
Arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and
smallest positive missing number is 1.

'''


def findTwoElement(arr, n):
    ans=[0]*2
    for i in range(n):
        if arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        else:
            ans[0] = abs(arr[i])

    for i in range(n):
        if arr[i]>0:
            ans[1]=i+1
    return ans


print(findTwoElement([2,3,4,4,5],5))




