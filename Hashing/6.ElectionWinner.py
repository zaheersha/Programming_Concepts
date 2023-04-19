'''
Given an array of names (consisting of lowercase characters) of candidates in an election.
A candidate name in array represents a vote casted to the candidate. Print the name of
candidate that received Max votes. If there is tie, print lexicographically smaller name.

Example 1:

Input:
n = 13
Votes[] = {john,johnny,jackie,johnny,john
jackie,jamie,jamie,john,johnny,jamie,
johnny,john}
Output: john 4
Explanation: john has 4 votes casted for
him, but so does johny. john is
lexicographically smaller, so we print
john and the votes he received.
'''
from collections import OrderedDict


def win(arr, n):
    # init
    mp = OrderedDict({})

    for i in arr:
        mp[i] = mp.get(i, 0) + 1

    maxx = -1
    ans = ""

    mp = OrderedDict(sorted(mp.items()))

    for key, value in mp.items():

        if value > maxx:
            maxx = value
            ans = key

    result = [ans, maxx]

    return result

print(win(["john","johnny","jackie","johnny","john"
"jackie","jamie","jamie","john","johnny","jamie",
"johnny","richard"],13))



