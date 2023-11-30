class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next
    
def mergeSort(head):
    if not head or not head.next:
        return head
    
    middle = getMiddle(head)
    leftHalf = head
    rightHalf = middle.next
    middle.next = None

    leftSorted = mergeSort(leftHalf)
    rightSorted = mergeSort(rightHalf)

    return merge(leftSorted,rightSorted)

def getMiddle(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left,right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.value < right.value:
            current.next = left
            left = left.next
        else: 
            current.next = right
            right = right.next
        
        current = current.next
    
    if left:
        current.next = left
    
    elif right:
        current.next = right

    return dummy.next

def printLL(head):
    num = head
    while num:
        print(num.value,end="---> ")
        num = num.next
    print("None")

head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
print("Original LL: ")
printLL(head)

sortedHead = mergeSort(head)
print("Sorted LL: ")
printLL(sortedHead)