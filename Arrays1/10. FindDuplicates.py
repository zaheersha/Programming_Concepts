'''
# Given an array a[] of size N which contains elements
# from 0 to N-1, you need to find all the elements occurring more than once in the given array.

# Input:
# N = 5
# a[] = {2,3,1,2,3}
# Output: 2 3
# Explanation: 2 and 3 occur more than once
# in the given array.
'''

'''
1- Traverse the given array from i= 0 to n-1 elements
     Go to index arr[i]%n and increment its value by n.
2- Now traverse the array again and print all those 
   indexes i for which arr[i]/n is greater than 1.

'''

def duplicates(arr, n):
    for i in range(0,n):
        index = arr[i]%n
        arr[index] +=n

    flag = False
    res=[]
    for i in range(0,n):
        if (arr[i]//n)>1:
            res.append(i)
            flag=True

    if flag==False:
        res.append(-1)

    return res

print(duplicates([2,3,1,2,3],5))












