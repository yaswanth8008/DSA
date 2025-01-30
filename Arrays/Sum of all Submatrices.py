

# Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.





def solve(A):
    n = len(A)
    summ = 0
    for i in range(n):
        count = 0
        for j in range(n):
            count = (i+1)*(j+1)*(n-i)*(n-j)
            summ += count*A[i][j]
    return summ