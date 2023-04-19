# Given a number N, the task is to find the largest prime factor of that number.

# Input:
# N = 5
# Output:
# 5
# Explanation:
# 5 has 1 prime factor
# i.e 5 only.

# Input:
# N = 24
# Output:
# 3

def largPrimeNumber(N):
    num = 2

    while (num * num) <= N:
        if N % num == 0:  # num is equal to N or devides N evenly
            N = N//num
        else:
            num += 1
    return int(N)


print(largPrimeNumber(24))
