'''
Your task is to implement the function strstr.
The function takes two strings as arguments (s,x) and
locates the occurrence of the string x in the string s.
The function returns and integer denoting the first occurrence of the string x in s (0 based indexing).

Note: You are not allowed to use inbuilt function.

Input:
s = ProgramingDoesGood, x = Does
Output: 10

A simple solution is to check one by one for every index of s. For every index, check if x is present.
'''

def strstr(s,x):

    ind_s=0

    while ind_s < len(s):

        if s[ind_s]  == x[0]:
            ind_p= 0
            temp_s= ind_s

            while temp_s <len(s) and s[temp_s] == x[ind_p]:

                ind_p += 1
                temp_s+= 1

                if ind_p == len(x):
                    return ind_s

        ind_s+= 1

    return -1

print(strstr("ProgramingDoesGood", "Does"))






