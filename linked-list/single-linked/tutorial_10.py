# deleting a node by a value
# deleteByValue()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def printLL(self):
        if self.head is None:
            print("LL is empty")
            return
        num = self.head
        while num is not None:
            print(num.data,"--->",end=" ")
            num = num.next
        
    def addEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        num = self.head
        while num.next is not None:
            num = num.next
        num.next = newNode

    def deleteByValue(self,value):
        if self.head is None:
            print("can't delete LL is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        num = self.head
        while num.next is not None:
            if num.next.data == value:
                break
            num = num.next
        if num.next is None:
            print("Node is not present") 
            return
        num.next = num.next.next



LL = LinkedList()
LL.addEnd(10)
LL.addEnd(14)
LL.addEnd(13)
LL.addEnd(30)
LL.addEnd(19)
LL.addEnd(17)




LL.deleteByValue(14)

LL.printLL()
