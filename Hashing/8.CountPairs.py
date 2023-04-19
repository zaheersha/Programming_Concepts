'''
Given an array of N integers, and an integer K, find the number
of pairs of elements in the array whose sum is equal to K.


Example 1:

Input:
N = 4, K = 6
arr[] = {[1, 5, 7, 1]}
Output: 2
Explanation:
arr[0] + arr[1] = 1 + 5 = 6
and arr[1] + arr[3] = 5 + 1 = 6.

Use a hash map to solve the question in O(n) time.

Create a map to store frequency of each number in the array. (Single traversal is required)
For every element check if it can be combined with any other element
(other than itself!) to give the desired sum. Increment the counter
 accordingly. After completion of second traversal, we’d have twice the
 required value stored in counter because every pair is counted two times.
Also take care of pairs with duplicate elements like (2,2) when K =4.

'''

def getPair(arr, n, sum):
    m = dict()

    for i in range(n):
        if arr[i] in m.keys():
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1

    twice_count = 0

    for i in range(0,n):
        if(sum-arr[i]) in m.keys():
            twice_count += m[sum - arr[i]]

        if sum - arr[i] == arr[i]:
            twice_count -= 1

    return int(twice_count/2)

print(getPair([1, 5, 7, 1], 4, 6))







