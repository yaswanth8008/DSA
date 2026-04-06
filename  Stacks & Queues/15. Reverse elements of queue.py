# Given an array of integers A and an integer B, we need to reverse the order of the first B elements of the array, 
# leaving the other elements in the same relative order. 

# NOTE: You are required to the first insert elements into an auxiliary queue then perform Reversal of first B elements.


from collections import deque

def solve(A, B):
    q = deque()
    for i in range(B-1,-1,-1):
        q.append(A[i])
    for i in range(B):
        A[i] = q.popleft()
    return A



A = [4,5,6,3,45,2,1,4,2,45,67]
B = 4

print(solve(A,B))