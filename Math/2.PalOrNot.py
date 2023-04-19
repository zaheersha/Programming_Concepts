# Given a number N.Find if the digit sum(or sum of digits) of N is a Palindrome number or not.
# Note:A Palindrome number is a number which stays the same when reversed.Example- 121,131,7 etc.
#
# Input:
# N=56
# Output:
# 1
# Explanation:
# The digit sum of 56 is 5+6=11.
# Since, 11 is a palindrome number.Thus,
# answer is 1.

def isPalindrome(N):
    newNum = 0
    while(N>0):
        newNum+=N%10
        N//=10
    revNewNum=0
    N=newNum
    while(N>0):
        revNewNum=revNewNum*10+N%10
        N//=10
    return 1 if revNewNum==newNum else 0

print(isPalindrome(N=9292))

#22

