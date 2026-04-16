# Given preorder and inorder traversal of a tree, construct the binary tree.

# NOTE: You may assume that duplicates do not exist in the tree.


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None



def buildTree(A, B):
    p_s = 0
    p_e = len(A) -1 
    i_s = 0
    i_e = len(A) - 1
    def find_i_x(arr,k,s,e):
        for i in range(s,e+1):
            if arr[i] == k:
                return i
    def construct_tree(A,B,p_s,p_e,i_s,i_e):
        if p_s > p_e or i_s > i_e:
            return None 
        new_node = TreeNode(A[p_s])
        i_x = find_i_x(B,A[p_s],i_s,i_e)
        n = i_x - i_s
        new_node.left = construct_tree(A,B,p_s + 1,p_s + n,i_s,i_x - 1)
        new_node.right = construct_tree(A,B,p_s + n + 1,p_e,i_x + 1,i_e)
        return new_node 
    return construct_tree(A,B,p_s,p_e,i_s,i_e) 


A = [5,7,9,12,8,13,15]
B = [9,7,12,5,8,13,15]

print(buildTree(A,B).val)