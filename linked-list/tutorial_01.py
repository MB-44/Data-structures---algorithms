# Singly-linked list

# Node class
class Node:
    # function to initialise the node object
    def __init__(self,data):
        self.data = data # assign data
        self.next = None # Initialize next as null
    

# linked-list class
class LinkedList:
    # function to Initialize the linked list object
    def __init__(self):
        self.head = None
    
    # function to insert a new at the beginning
    def push(self,newData):
        # 1. Allocate the node
        # 2. Put in the data
        newData = Node(newData)

        # 3. Make next of new node as head
        newData.next = self.head

        # 4. Move the head to point to new Node
        self.head = newData
    
    # This function is in LinkedList class
    # Inserts a new Node after the given previous node. 
    # This method is defind inside LinkedList class shown above
    def insertAfter(self,previousNode, newData):
        # 1. check if the given previousNode exists
        if previousNode is None:
            print("The given previous node must in LinkedList")
            return

        # 2. create new node
        # 3. Put in the data
        newData = Node(newData)

        # 4. Make next of new Node as next of previousNode
        newData.next = previousNode.next

        # 5. Make next of previousNode as newNode
        previousNode.next = newData
    
    # This function is defined in linked list class
    # appends a new node at the end. This method is \ 
    # defined inside LinkedList class shown above
    def append(self,newData):
        # 1. Create a new node
        # 2. put in the data
        # 3. Set next as none
        newData = Node(newData)

        # 4. If the linked list is empty, \
        # then make the new node a head
        if self.head is None:
            self.head = newData
            return
        
        # 5. else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
        
        # 6. change the next of last node
        last.next = newData
        