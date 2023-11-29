# adding a node to the beginning of the linked list
# addBegin()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def printLL(self):
        if self.head is None:
            print("Linked list is empty")
        else: 
            num = self.head
            while num is not None:
                print(num.data)
                num = num.ref
    
    def addBegin(self,data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head = newNode

LL1 = LinkedList()
LL1.addBegin(10)
LL1.addBegin(12)
LL1.printLL()