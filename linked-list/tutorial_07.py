# adding node to empty linked list

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
    
    
    def InsertEmpty(self,data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else: 
            print("Linked list is not empty")