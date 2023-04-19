#For a given number N check if it is prime or not.
# A prime number is a number which is only divisible by 1 and itself.
#
# Input:
# N = 25
# Output:
# 0

def isPrime (N):
    if(N == 1):
        return 0

    num =2
    while(num*num <= N):
        if(N % num == 0):
            return 0
        num+=1
    return 1

print(isPrime(1))




