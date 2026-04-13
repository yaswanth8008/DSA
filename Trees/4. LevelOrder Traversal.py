# Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        q = deque()
        q.append(A)
        l = []
        while len(q) != 0:
            size = len(q)
            elements = []
            for i in range(size):
                f = q[0]
                elements.append(f.val)
                q.popleft()
                if f.left != None:
                    q.append(f.left)
                if f.right != None:
                    q.append(f.right)
            l.append(elements)
        return l