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
                print(num.data,"--->",end=" ")
                num = num.next
    
    def addEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else: 
            num = self.head
            while num.next is not None:
                num = num.next
            num.next = newNode

    def deleteBegin(self):
        if self.head is None:
            print("linked list is empty, we can't delete nodes!")
            return
        self.head = self.head.next

LL1 = LinkedList()
LL1.addEnd(10)
LL1.addEnd(11)
LL1.addEnd(12)
LL1.addEnd(13)
LL1.addEnd(14)
LL1.deleteBegin()
LL1.printLL()
