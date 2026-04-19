# You are given an integer array A denoting the Level Order Traversal of the Binary Tree.

# You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.

# NOTE:

# In the array, the NULL/None child is denoted by -1.

from collections import deque
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

def solve(A):
    i = 1
    q = deque()
    ans = TreeNode(A[0])
    q.append(ans)
    
    while len(q) != 0:
        front = q[0]
        q.popleft()
        if i < len(A):
            if A[i] != -1:
                left_node = TreeNode(A[i])
                front.left = left_node
                q.append(left_node)
            i += 1
            
            if A[i] != -1:
                right_node = TreeNode(A[i])
                front.right = right_node
                q.append(right_node)
            i += 1 
        else:
            break

    return ans