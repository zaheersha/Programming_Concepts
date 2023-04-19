'''
Given two strings A and B. Find the characters that are not common in the two strings.

Input:
A = characters
B = alphabets
Output: bclpr
Explanation: The characters 'b','c','l','p','r'
are either present in A or B, but not in both.
ord("z")
a   b ....w
97 98 ....122
'''


def UncommonChar(A, B):
    res = ''
    present = [0] * 26

    for e in A:
        present[ord(e) - ord('a')] = 1

    for e in B:
        if present[ord(e) - ord('a')] == 1 or present[ord(e) - ord('a')] == -1:
            present[ord(e) - ord('a')] = -1

        else:
            present[ord(e) - ord('a')] = 2

    for i, e in enumerate(present):
        if e == 1 or e == 2:
            res += chr(i + ord('a'))

    if res:
        return res
    else:
        return "Strings are the same"


print(UncommonChar("characters", "alphabets"))
