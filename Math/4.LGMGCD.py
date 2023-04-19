#Given two numbers A and B. The task is to find out their LCM and GCD.
# LCM is the smallest number divisible by all the given numbers.
#
# HCF/GCD is the largest number that can divide all the given numbers.
#
# LCM = a*b/HCF
# Input:
# A = 14 , B = 8
# Output:
# 56 2
# Explanation:
# LCM of 14 and 8 is 56, while
# thier GCD is 2.

import math

def lcmandGcd(A, B):
    arr = [0]*2

    g = math.gcd(A,B)
    l = (A*B)//g

    arr[0], arr[1] =l,g

    return arr

print(lcmandGcd(A=12, B=27))


