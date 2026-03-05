# Node class represents each element in the stack
class Node:
    def __init__(self, data):
        self.data = data      # store value
        self.next = None      # pointer to next node


# Stack class
class stack:

    def __init__(self):
        self.top = None       # top pointer (initially stack is empty)

    # PUSH operation
    def push(self, data):
        temp = Node(data)     # create new node
        temp.next = self.top  # link new node to previous top
        self.top = temp       # update top

    # POP operation
    def pop(self):
        if self.top == None:
            print("stack is Empty")
        else:
            print("poped element ==> ", self.top.data)
            self.top = self.top.next   # move top pointer

    # PEEK operation
    def peek(self):
        if self.top == None:
            print("Stack is empty")
        else:
            print("Top element ==> ", self.top.data)

    # DISPLAY operation
    def display(self):
        temp = self.top       # temporary pointer for traversal
        while temp:
            print("[", temp.data, "]")
            temp = temp.next


# main program
dis = stack()

dis.push(10)
dis.push(20)
dis.push(30)

dis.pop()
dis.peek()
dis.display()
