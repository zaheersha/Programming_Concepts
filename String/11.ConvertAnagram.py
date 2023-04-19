'''
Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to remove a
 character from any string. Find the minimum number of characters to be deleted to make both the strings anagram.
 Two strings are called anagram of each other if one of them can be converted into another by rearranging its letters.

Example 1:

Input:
S1 = bcadeh
S2 = hea
Output: 3
Explanation: We need to remove b, c
and d from S1.

Use frequency array to store occurence of characters and then check if both
the frequency array are same or not. Then remove the extra characters from both the strings.

'''


def remAnagram(str1, str2):
    alpha1 = [0] * 26
    alpha2 = [0] * 26

    for i in range(0, len(str1)):
        alpha1[ord(str1[i]) - ord('a')] += 1
    for i in range(0, len(str2)):
        alpha2[ord(str2[i]) - ord('a')] += 1

    result=0
    for i in range(0,26):
        result+=abs(alpha1[i] - alpha2[i])
    return result

print(remAnagram("bcadeh", "hea"))