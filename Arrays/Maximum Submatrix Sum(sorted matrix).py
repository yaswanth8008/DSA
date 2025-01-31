# Maximum Submatrix Sum

def solve(A):
    m = len(A[0])
    n = len(A)
    for i in range(n):
        for j in range(m-2,-1,-1):
            A[i][j] += A[i][j+1]
    for i in range(m):
        for j in range(n-2,-1,-1):
            A[j][i] += A[j+1][i]
    max_sum = -1000000
    for i in range(n):
        for j in range(m):
            max_sum = max(max_sum,A[i][j])
    return max_sum