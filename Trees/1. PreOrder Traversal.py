# Given a binary tree, return the preorder traversal of its nodes values.


# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


	# @param A : root node of tree
	# @return a list of integers
def preorderTraversal(self,A):
    l = []
    def pre_order(A):
        if A == None:
            return
        l.append(A.val)
        pre_order(A.left)
        pre_order(A.right)
    pre_order(A)
    return l