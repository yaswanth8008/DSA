


def solve(A):
    n = len(A)
    m = len(A[0])
    summs = []
    maximum_sum_submatrix = -100000
                
    def kadane(arr):
        curr_sum = 0
        max_sum = -10000000
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum >= max_sum:
                max_sum = curr_sum 
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
    for i in range(n):
        arr_sum = [0]*m
        for j in range(i,n):
            for k in range(m):
                arr_sum[k] += A[j][k]
            maximum_sum_submatrix = max(maximum_sum_submatrix,kadane(arr_sum))
    return maximum_sum_submatrix