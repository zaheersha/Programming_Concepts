'''
In this problem, a String S is composed of lowercase alphabets and wildcard characters i.e. '?'.
Here, '?' can be replaced by any of the lowercase alphabets. Now you have to classify the given String on the basis of following rules:
If there are more than 3 consonants together or more than 5 vowels together, the String is considered to be "BAD".
A String is considered "GOOD" only if it is not “BAD”.
NOTE: String is considered as "BAD" if the above condition is satisfied even once. Else it is "GOOD" and the task is to make the string "BAD".

Example 1:

Input:
S = mobile??
Output:
GOOD
Explanation: The String doesn't contain more
than 3 consonants or more than 5 vowels together.
So, it's a GOOD string.
Example 2:

Input:
S = bcdaeiou??
Output:
BAD
Explanation: The String contains the
Substring "aeiou??" which counts as 7
vowels together. So, it's a BAD string.
'''

def isGoodBad(S):

    #Init
    vow=0
    con=0
    flag=0

    for i in range(len(S)):
        if S[i]== 'a' or S[i]== 'e' or S[i]== 'i' or S[i] == 'o' or S[i] == 'u':
            vow+=1
            con=0
        elif(S[i]!='a' and S[i]!='e' and S[i]!='i' and S[i] !='o' and S[i] !='u' and S[i]!='?'):
            vow=0
            con+=1

        if(S[i]=='?'):
            con+=1
            vow+=1

        if(vow>5 or con>3):
            flag=1
            break
    if(flag==1):
        return "BAD"
    else:
        return "GOOD"

print(isGoodBad("hello???"))










