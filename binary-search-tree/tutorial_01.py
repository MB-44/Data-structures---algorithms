# Binary search tree
# left is always less and right is always greater

class TreeNode:
    def __init__(self,value):
        self.left  = None
        self.right = None
        self.value = value
        self.content = None

    def insert(self,value, content=None):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                self.left.content = content
            else: 
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = TreeNode(value)
                self.right.content = content
            else: 
                self.right.insert(value, content)

    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        print(self.value)
        if self.right:
            self.right.inOrderTraversal()

    def preOrderTraversal(self):
        print(self.value)
        if self.left:
            self.left.inOrderTraversal()
        print(self.value)
        if self.right:
            self.right.preOrderTraversal()

    def postOrderTraversal(self):
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()
        print(self.value)


    def find(self,value):
        if value < self.value:
            if self.left is None:
                return None
            else: 
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else: 
                return self.right.find(value)
        else:
            return self


tree = TreeNode(15)
tree.insert(10)
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(2)
tree.insert(18)
tree.insert(21)
tree.insert(16, {"name": "MB-44"})



# tree.inOrderTraversal()
# tree.preOrderTraversal()
# tree.postOrderTraversal()

found = tree.find(16).content['name']
print(found)
