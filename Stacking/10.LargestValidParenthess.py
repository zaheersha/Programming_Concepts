'''
Given a string S consisting of opening and closing parenthesis '(' and ')'.
 Find length of the longest valid parenthesis substring.

A parenthesis string is valid if:

For every opening parenthesis, there is a closing parenthesis.
Opening parenthesis must be closed in the correct order.
Example 1:

Input: S = ((()
Output: 2
Explaination: The longest valid
parenthesis substring is "()".
'''


def maxParenteses(str1):
    n = len(str1)
    stk = [-1]
    result = 0

    for i in range(n):

        if str1[i] == "(":
            stk.append(i)
        else:
            if len(stk) != 0:
                stk.pop()
            if len(stk) != 0:
                result = max(result, i - stk[len(stk)-1])
            else:
                stk.append(i)
    return result

print(maxParenteses("(()())))"))


