# Given a number N.Check whether it is a triangular number or not.
# Note: A number is termed as a triangular number if we can represent it in the
# form of a triangular grid of points such that the points form an equilateral
# triangle and each row contains as many points as the row number, i.e., the first
# row has one point, the second row has two points, the third row has three points and so on.
# The starting triangular numbers are 1, 3 (1+2), 6 (1+2+3), 10 (1+2+3+4).
# Input:
# N=55
# Output:
# 1
#2*N = sqrt(2*N)*(sqrt(2*N)+1)
import math


def isTriangular(N):
    x = int(math.sqrt(2 * N))
    if x*(x+1) == 2*N:
        return 1
    return 0

print(isTriangular(11))

