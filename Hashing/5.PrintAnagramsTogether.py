'''
Given an array of strings, return all groups of strings that are anagrams.
The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.


Example 1:

Input:
N = 5
words[] = {act,god,cat,dog,tac}
Output:
god dog
act cat tac
Explanation:
There are 2 groups of
anagrams "god", "dog" make group 1.
"act", "cat", "tac" make group 2.
'''
from collections import defaultdict


def Anagrams(s):

    d=defaultdict(list)

    for i,e in enumerate(s):
        e=str(sorted(e))
        d[e].append(s[i])

    res = []
    for l in d.values():
        res.append(l)
    return res

print(Anagrams(['act','god','cat','dog','tac']))