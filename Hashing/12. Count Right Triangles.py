# Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.

# Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right-angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.

# NOTE: The answer may be large so return the answer modulo (109 + 7).


def solve(A, B):
    h_x = {}
    h_y = {}
    count = 0
    for i in A:
        h_x[i] = h_x.get(i,0) + 1
    for j in B:
        h_y[j] = h_y.get(j,0) + 1
    for i in range(len(A)):
        count += (h_x[A[i]]-1)*(h_y[B[i]]-1)
    return count % (10**9+7)