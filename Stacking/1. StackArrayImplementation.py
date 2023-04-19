'''
Write a program to implement a Stack using Array. Your task is to use the class
as shown in the comments in the code editor and complete the functions push()
and pop() to implement a stack.

Example 1:

Input:
push(2)
push(3)
pop()
push(4)
pop()
Output: 3, 4
Explanation:
push(2)    the stack will be {2}
push(3)    the stack will be {2 3}
pop()      poped element will be 3,
           the stack will be {2}
push(4)    the stack will be {2 4}
pop()      poped element will be 4
'''

class MyStack:

    def __init__(self):
        self.arr=[]

    def push(self,data):
        self.arr.append(data)

    def pop(self):
        if len(self.arr)==0:
            return -1
        return self.arr.pop()

p1 = MyStack()
p1.push(2)
p1.push(3)
p1.push(4)
print(p1.arr)
p1.pop()
print(p1.arr)






















