'''
Let's give it a try! You have a linked list and you have to implement the functionalities
push and pop of stack using this given linked list. Your task is to use the class as shown
in the comments in the code editor and complete the functions push() and pop() to implement a stack.

Example 1:

Input:
push(2)
push(3)
pop()
push(4)
pop()
Output: 3 4
Explanation:
push(2)    the stack will be {2}
push(3)    the stack will be {2 3}
pop()      poped element will be 3,
           the stack will be {2}
push(4)    the stack will be {2 4}
pop()      poped element will be 4
'''


class StackNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        return

    def pop(self):
        if self.isEmpty():
            return -1

        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def printList(self):
        temp = self.root
        while temp:
            print(temp.data)
            temp = temp.next


p1 = MyStack()
p1.push(3)
p1.push(2)
p1.push(1)
p1.printList()
p1.pop()
p1.printList()

