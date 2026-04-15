# Given a binary tree of integers denoted by root A. Return an array of integers representing the right view of the Binary tree.

# Right view of a Binary Tree is a set of nodes visible when the tree is visited from Right side.


from collections import deque

def solve(A):
    q = deque()
    q.append(A)
    l = []
    while len(q) != 0:
        size = len(q)
        for i in range(size):
            f = q[0]
            q.popleft()
            if i == size - 1:
                l.append(f.val)
            if f.left != None:
                q.append(f.left)
            if f.right != None:
                q.append(f.right)
    return l