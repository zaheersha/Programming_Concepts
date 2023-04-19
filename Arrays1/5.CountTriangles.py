# Given an unsorted array arr[] of n positive integers.
# Find the number of triangles that can be formed with three
#     different array elements as lengths of three sides of triangles.
# Input:
# n = 3
# arr[] = {6,4,9,7,8}
# Output:
# 10
# Explanation:
# A triangle is possible
# with all the elements 5, 3 and 4.
#1. Sort the elements of the array. Sorting would help you to maintain the condition that  for any three sides of  the triangle  a,b and c ,
#
#    max(a,b) <=c.
#
# 2. Now, traverse for each pair of element in the array and make the count of triplets such that (a+b)>c.


def findNumberTriangles(arr, n):
    arr.sort()
    count =0

    for i in range(n-2):
        k=i+2

        for j in range(i+1,n):

            while(k<n and arr[i] + arr[j]>arr[k]):
                k+=1
                count+=k-j-1

    return count

print(findNumberTriangles([6,4,9,7,8],5))
























