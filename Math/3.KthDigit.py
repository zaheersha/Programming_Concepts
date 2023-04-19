# Given two numbers A and B, find Kth digit from right of A^B.
# Example
# Input:
# A = 3
# B = 3
# K = 1
# Output:
# 7
# Explanation:
# 3^3 = 27 and 1st digit from right is 7
#256
#25
#2
def kthDigit(A,B,K):
    x=pow(A,B)
    temp = 0
    while(K>0):
        temp = x%10
        x=x//10
        K-=1
    return  temp

print(kthDigit(A=5345, B=342, K=5))

S=pow(5345,342)
print(S)





