# Maximum Sum Square SubMatrix


# https://www.interviewbit.com/problems/maximum-sum-square-submatrix/



def Maximum_Sum_Square_SubMatrix (A, B):

    def max_sum_window(arr,k):
            curr_sum = 0
            n = len(arr)
            for i in range(n):
                curr_sum += arr[i]
                arr[i] = curr_sum
            max_sum = arr[k-1]
            for j in range(k,n):
                max_sum = max(max_sum,arr[j]-arr[j-k])
            return max_sum

    n = len(A)
    maximum_sum = -10000000
    for i in range(n):
        arr = [0]*n
        for j in range(i,n):
            for k in range(n):
                arr[k] += A[j][k]
            if j - i + 1 == B:
                maximum_sum = max(maximum_sum,max_sum_window(arr,B))
    return maximum_sum
