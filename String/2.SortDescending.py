'''
Given a string str containing only lower case alphabets, the task is to sort it in lexicographically-descending order.
Input: str = "fora"
Output: "rofa"
Explanation: "rof" is in
lexicographically-descending order.
'''

def ReverseSort(str):
    charCount=[0]*26
    for i in str:
        charCount[ord(i)-ord('a')]+=1
    str=''
    for i in range(25,-1,-1):
        for j in range(charCount[i]):
            str+=chr(ord('a') + i)
    return str

print(ReverseSort("fora"))


