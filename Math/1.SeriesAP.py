# Given the first 2 terms A1 and A2 of an Arithmetic Series.Find the Nth term of the series.
#
# Input:
# A1=2
# A2=4
# N=4
# Output:
# 8
# Explanation:
# The series is 2,4,6,8,10....
# Thus,4th term is 5.

def SeriesAP (A1, A2, N):
    differece = A2-A1
    nTerm = A1+(N-1)*differece
    return nTerm

nTerm = SeriesAP(A1=2, A2=4,N=6)
print(nTerm)













