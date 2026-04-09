# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None


def postorderTraversal(self, A):
    l = []
    def post_order(A):
        if A == None:
            return
        post_order(A.left)
        post_order(A.right)
        l.append(A.val)
    post_order(A)
    return l
