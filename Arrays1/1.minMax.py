# Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.
#
# Input:
# N = 6
# A[] = {3, 2, 1, 56, 10000, 167}
# Output:
# min = 1, max =  10000

def getMinMax (arr, n):

    #Intialization
    #even number of elements in the array
    if(n % 2 == 0):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        i=2
        #odd number of elements in the array
    else:
        mx=mn=arr[0]
        i = 1

    #processing
    while(i < n-1):
        if arr[i] < arr[i+1]:
            mx = max(mx, arr[i+1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i+1])

        i+=2

    #returning
    return (mx, mn)

N= 6
A=[3,2,1,56,10000,167]

print(getMinMax(A,N))
















