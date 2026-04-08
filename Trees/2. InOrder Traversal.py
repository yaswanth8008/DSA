
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None






class Solution:

    def __init__(self,A):
        self.l = []
        self.A = A
   

    def inorderTraversal(self, A):
        if A == None:
            return
        self.inorderTraversal(A.left)
        self.l.append(A.val)
        self.inorderTraversal(A.right)
        return self.l