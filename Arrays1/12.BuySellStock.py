'''
The cost of stock on each day is given in an array A[] of size N.
Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
Note: There may be multiple possible solutions. Return any one of them.
Any correct solution will result in an output of 1, whereas wrong solutions will result in an output of 0.

Example 1:

Input:
N = 7
A[] = {100,180,260,310,40,535,695}
Output:
1
Explanation:
One possible solution is (0 3) (4 6)
We can buy stock on day 0,
and sell it on 3rd day, which will
give us maximum profit. Now, we buy
stock on day 4 and sell it on day 6.
'''

def stockBuySell(A,N):

    result= []
    if(N==1):
        return  result

    i=0
    cnt=0

    while(i<N-1):
        while((i<N-1) and (A[i+1]<=A[i])):
            i=i+1
        if(i==N-1):
            break

        e=[0,0]
        e[0]=i
        i=i+1

        while((i<N) and A[i] >=A[i-1]):
            i=i+1
        e[1]=i-1
        result.append([e[0],e[1]])
        cnt=cnt+1

        if(cnt==0):
            return []
        else:
            return result


print(stockBuySell([100,180,260,310,40,535,695],7))






