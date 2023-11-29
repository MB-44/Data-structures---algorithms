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

    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            return
        num = self.head
        while num.next is not None:
            if num.next.data == x:
                break
            num = num.next
        if num.next is None:
            print("Node is not found")
        else: 
            newNode = Node(data)
            newNode.data = num.next
            num.next = newNode


LL1 = LinkedList()
LL1.addEnd(10)
LL1.add_before(20,10)
LL1.printLL()