#For an integer N find the number of trailing zeroes in N!.
# Input:
# N = 5
# Output:
# 1
# Explanation:
# 5! = 5*4*3*2*1 = 120 so the number of trailing zero is 1.

def trailingZeros(N):
    j=5
    ans = 0
    while j<=N:
        ans = ans + N//j
        j=j*5
    return ans

print(trailingZeros(5))