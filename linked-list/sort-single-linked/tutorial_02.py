class Node: 
    def __init__(self,data=0,next=None):
        self.data = data 
        self.next = next

def sortLinkedList(head):
    values = []
    current = head
    while current:
        values.append(current.data)
        current = current.next
    values.sort()

    sortedHead = None
    for value in reversed(values):
        sortedHead = Node(value,sortedHead)
    return sortedHead

def printLL(head):
    current = head
    while current:
        print(current.data, end="---> ")
        current = current.next
    print("None")

head = Node(4, Node(3, Node(2, Node(1))))
print(f"Original LL: ")
printLL(head)

headSorted = sortLinkedList(head)
print(f"Sorted LL: ")
printLL(sortLinkedList)