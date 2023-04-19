'''
Given two strings S1 and S2 as input, the task is to merge them alternatively i.e.
 the first character of S1 then the first character of S2 and so on till the strings end.
NOTE: Add the whole string if other string is empty.

Example 1:

Input:
S1 = "Hello" S2 = "Bye"
Output: HBeylelo
Explanation: The characters of both the
given strings are arranged alternatlively.
'''

def mergeStr(S1,S2):
    #Initialization
    res=''
    i=0
    j=0

    #Loops
    while i<len(S1) and j< len(S2):
        res+=S1[i]
        res+=S2[j]
        i+=1
        j+=1

    while i < len(S1):
        res+=S1[i]
        i+=1
    while j < len(S2):
        res += S2[j]
        j+=1

    return res

print(mergeStr("Hello", "Bye"))










