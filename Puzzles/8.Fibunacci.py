# Given a number N. Find the last two digits of the Nth fibonacci number.
# Note: If the last two digits are 02, return 2.
# The last two digits of a fibonacci number repeats after an interval of 300 i.e
# the 1000th and 1300th fibonacci numbers have the same last two digits.
# Input:
# N = 13
# Output:
# 33
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144,233

def fibunacciDigits(N):
    fib=[0]*300
    fib[0]=0
    fib[1]=1
    for i in range(2,min(299,N)+1):
        fib[i]=(fib[i-1]+fib[i-2])%100
    return fib[(N%300)]


# print(fibunacciDigits(56456345))


def fb(n):
    if n<=1:
        return n
    else:
        return(fb(n-1) + fb(n-2))



# print(fb(5))


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

print(fb(9))




