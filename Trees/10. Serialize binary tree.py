# Given the root node of a Binary Tree denoted by A. You have to Serialize the given Binary Tree in the described format.

# Serialize means encode it into a integer array denoting the Level Order Traversal of the given Binary Tree.

# NOTE:

# In the array, the NULL/None child is denoted by -1.
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

from collections import deque

def solve(A):
    arr = []
    q = deque()
    q.append(A)
    while len(q) != 0:
        front = q[0]
        q.popleft()
        if front == None:
            arr.append(-1)
        else:
            q.append(front.left)
            q.append(front.right)
            arr.append(front.val) 
    return arr