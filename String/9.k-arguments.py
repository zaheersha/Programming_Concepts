'''

Given two strings of lowercase alphabets and a value K, your task is to complete the given function which
tells if  two strings are K-anagrams of each other or not.

Two strings are called K-anagrams if both of the below conditions are true.
1. Both have same number of characters.
2. Two strings can become anagram by changing at most K characters in a string.

Input:
str1 = "fodr", str2="gork"
k = 2
Output:
1
Explanation: Can change fd to gk

Stores occurrence of all characters of both strings in separate count arrays.
Count number of different characters in both strings (in this if a strings has 4 a
and second has 3 ‘a’ then it will be also count.
If count of different characters is less than or equal to k, then return true else false.
'''


def areKArguments(str1, str2, k):
    if len(str1) != len(str2):
        return False

    n = len(str1)
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(n):
        c1[ord(str1[i]) - 97] += 1
        c2[ord(str2[i]) - 97] += 1
    cnt = 0
    for i in range(26):
        if c1[i] > c2[i]:
            cnt += abs(c1[i] - c2[i])

    return cnt <= k

print(areKArguments("fodr", "gork", 2))