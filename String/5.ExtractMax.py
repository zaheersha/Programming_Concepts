'''
Given a alphanumeric string S, extract maximum numeric value from S.

Example 1:

Input:
S = 100klh564abc365bg
Output: 564
Explanation: Maximum numeric value
among 100, 564 and 365 is 564.

Initialise num=0 and for every time you encounter a consecutive digit use
num = num * 10 + (S[i]-'0');
'''


def extractMaximum(str1):
    # Initialization
    num, res, flag = 0, 0, 0

    for i in range(len(str1)):
        if "0" <= str1[i] <= "9":
            num = num * 10 + int(int(str1[i]) - 0)
            flag = 1
        else:
            res = max(res, num)
            num = 0
    if flag == 1:
        return max(res, num)
    else:
        return -1


# print(extractMaximum("100klh564abc365bg"))









def finNum(s1):
    res = ''
    cur='0'
    flag = -1
    for c in s1:
        if '0' <= c <= '9':
            res+=c
            flag =1
        else:
            if res == '':
                res = '0'
            maxVal = max(int(res),int(cur))
            cur = maxVal
            res = ''

    if flag == 1:
        return max(int(maxVal), int(res), int(cur))
    else:
        return  flag

print(finNum("100klh564abc365bg900"))






