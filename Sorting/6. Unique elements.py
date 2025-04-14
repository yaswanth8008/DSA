# You are given an array A of N elements. You have to make all elements unique. 
# To do so, in one step you can increase any number by one.
# Find the minimum number of steps.


def solve(A):
    cnt = 0
    A.sort()
    for i in range(1,len(A)):
        if A[i] <= A[i-1]:
            temp = A[i]
            A[i] = A[i-1] + 1
            cnt += A[i] - temp
            
    return cnt


print(solve([21,23,5,10,19,13,12,21,21,7,21]))