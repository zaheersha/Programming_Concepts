'''
Find the first non-repeating element in a given array arr of N integers.
Note: Array consists of only positive and negative integers and not zero.

Example 1:

Input : arr[] = {-1, 2, -1, 3, 2}
Output : 3
Explanation:
-1 and 2 are repeating whereas 3 is
the only number occuring once.
Hence, the output is 3.

An Efficient Solution is to use hashing.
1) Traverse array and insert elements and their counts in hash table.
2) Traverse array again and print first element with count equals to 1.
'''


def allNonRepeating(arr, n):
    mp=dict()

    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1

    ans = []
    for i in range(n):
        if mp[arr[i]] == 1:
            ans.append(arr[i])

    if ans != []:
        return ans
    else:
        return "No Repeating Elements"


print(allNonRepeating([-1, 2, -1, 3, 2, 7], 6))
