# Emplement stacks using LIST

# Push - which allow us to add the element to the stack
# when we are using list for stacks -
# push --> append
# pop ---> pop

stack = []

def push():
    if len(stack) == n:
        print("list is full")
    else: 
        element = input("Enter your element: ")
        stack.append(element)
        print(stack)

def pop():
    if not stack:
        print("stack is empty")
    else: 
        removeElement = stack.pop()
        print(f"Removed element is: {removeElement}")
        print(stack)

n = int(input("limit of stack: "))
while True:
    print("--Select the operations 1.push 2.pop 3.quit--")
    choice = int(input(": "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else: 
        print("Enter the correct operation!")






