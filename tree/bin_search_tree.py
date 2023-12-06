# Binary Search Tree

# Left subtree of a node contains only nodes with keys lesser than node's key
# right subtree of node contains only nodes with key greater than node's key
# the left subtree and right subtree each must also be a BST

# -----------------

# Search
# wheather check BST contain given value
# 1. check is the bst is empty
# 2. root == given value ---> yes
# 3. given_value < rootkey ---> search left subtree again step 1
# 4. given_value > rootkey ---> search right subtree again step 1

# Insertion
# check bst is empty ---> rootNode = newNode
# root < new_node ---> right subtree
# root > new_node ----> left subtree

# Deletion
# bst empty --> can't delete

# 1st case - deletion (no child)
# given_value > rootnode ---> right subtree
# if given_value = leafNode ---> delete it

# 2nd case - deletion (1 child node)
# given_value > rootNode ---> right subtree
# remove the given_value
# replace it with the child

# 3rd case - deletion (2 child node)
# given_value < rootNode ---> left subtree
# if i put largest child in the where given_value was
# other small value will be left side 


# Traversing a BST
