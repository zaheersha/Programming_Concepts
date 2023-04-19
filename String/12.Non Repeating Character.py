'''
Given a string S consisting of lowercase Latin Letters. Find the first non-repeating character in S.

Example 1:

Input:
S = lohello
Output: h
Explanation: In the given string, the
first character which is non-repeating
is h, as it appears first and there is
no other 'h' in the string.

Store the count of each character in a hash table.

Iterate over the string and if the frequency of any
character is 1, return it. If there is no non-repeating character then we return '$'.

'''


def nonRepeating(s):
    # hash table
    occurances = [0 for i in range(256)]

    for char in s:
        occurances[ord(char)] += 1

    for i in range(len(s)):
        if occurances[ord(s[i])] == 1:
            return s[i]

    return "No Repeating Characters"

print(nonRepeating("hhello"))


def nonRep(str1):
    arr1=26*[0]
    for i in range(len(str1)):
        arr1[ord(str1[i]) - ord("a")] +=1

    for c in range(len(str1)):
        if arr1[ord(str1[c]) - ord('a')] == 1:
            return str1[c]

print(nonRep("loshello"))


