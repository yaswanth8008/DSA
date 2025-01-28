# Given a matrix of integers A of size N x M and multiple queries Q, for each query, find and return the submatrix sum.

# Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

# NOTE:

# Rows are numbered from top to bottom, and columns are numbered from left to right.
# The sum may be large, so return the answer mod 109 + 7.
# Also, select the data type carefully, if you want to store the addition of some elements.
# Indexing given in B, C, D, and E arrays is 1-based.
# Top Left 0-based index = (B[i] - 1, C[i] - 1)
# Bottom Right 0-based index = (D[i] - 1, E[i] - 1)


def solve(self, A, B, C, D, E):
    sum_submatrices = []
    rows = len(A)
    columns = len(A[0])
    for i in range(rows):
        for j in range(1,columns):
            A[i][j] += A[i][j-1]
    for i in range(columns):
        for j in range(1,rows):
            A[j][i] += A[j-1][i]
    for i in range(len(B)):
        a1 = B[i] - 1
        b1 = C[i] - 1
        a2 = D[i] - 1
        b2 = E[i] - 1
        summ = A[a2][b2]
        if a1 > 0:
            summ -= A[a1-1][b2]
        if b1 > 0:
            summ -= A[a2][b1-1] 
        if a1 > 0 and b1 > 0:
            summ += A[a1-1][b1-1]
        summ = summ%(10**9+7)
        sum_submatrices.append(summ)
    return sum_submatrices 