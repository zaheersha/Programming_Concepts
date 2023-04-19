# Given an integer x, find the square root of x.If x is not a perfect square, then return floor(√x).
#
# Example
# 1:
#
# Input:
# x = 5
# Output: 2
# Explanation: Since, 5 is not a
# perfect
# square, floor
# of
# square_root
# of
# 5 is 2.

# 1) Start with ‘start’ = 0, end = ‘x’,
# 2) Do following while ‘start’ is smaller than or equal to ‘end’.
#       a) Compute ‘mid’ as (start + end)/2
#       b) compare mid*mid with x.
#       c) If x is equal to mid*mid, return mid.
#       d) If x is greater, do binary search between mid+1 and end. In this case, we also update ans (Note that we need floor).
#       e) If x is smaller, do binary search between start and mid

def fSQRT(x):

      if x == 0 or x == 1:
            return x
      #Initialization
      start = 1
      end = x
      res = 0

      while start <= end:
            mid = (start + end)//2

            if mid*mid == x:
                  return mid

            if mid*mid < x:
                  start = mid+1
                  res = mid
            else:
                  end = mid-1
      return res

print(fSQRT(67))