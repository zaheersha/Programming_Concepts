'''
You are given a string S, the task is to reverse the string using stack.



Example 1:


Input: S="GeeksforGeeks"
Output: skeeGrofskeeG
'''


def createStack():
    stack = []
    return stack


def size(stack):
    return len(stack)


def isEmpty(stack):
    if size(stack) == 0:
        return True


def push(stack, item):
    stack.append(item)


def pop(stack):
    if isEmpty(stack): return
    return stack.pop()


def reverse(string):
    n = len(string)

    stack = createStack()

    for i in range(0, n, 1):
        push(stack, string[i])

    string=""

    for i in range(0,n,1):
        string+=pop(stack)

    return string

print(reverse('GeeksforGeeks'))
