# Given a binary tree, return a 2-D array with vertical order traversal of it. Go through the example and image for more details.


# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque

def verticalOrderTraversal(A):
    d = dict()
    q = deque()
    pair = (A,0)
    q.append(pair)
    while len(q) != 0:
        size = len(q)
        for i in range(size):
            pair = q[0]
            f = pair[0]
            level = pair[1]
            if level not in d:
                d[level] = []
                
            d[level].append(f.val)
            q.popleft()
            if f.left != None:
                q.append((f.left,level - 1))
            if f.right != None:
                q.append((f.right,level + 1))
    min_level = min(d.keys())
    max_level = max(d.keys())
    ans = []
    for i in range(min_level,max_level+1):
        ans.append(d[i])
    return ans 