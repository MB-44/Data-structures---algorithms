# Traversal
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printL1(self):
        if self.head is None:
            print("linked list is empty")
        else: 
            num = self.head
            while num is not None:
                print(num)
                num = num.ref

l1 = LinkedList()
l1.printL1()