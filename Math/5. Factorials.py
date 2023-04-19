#Back-end complete function Template for Python 3


class Solution:
    def factorial (self, N):
        ans = 1
        # Calculating the factorial
        for i in range(2, N+1):
               ans = ans*i
        return ans