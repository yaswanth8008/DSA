# Given a sorted array of distinct integers A and an integer B, find and 
# return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.


def solve(A, B):
    cnt = 0
    i = 0
    j = len(A)-1
    while i < j:
        if A[i] + A[j] == B:
            cnt += 1
            i += 1
            j -= 1
        elif A[i] + A[j] > B:
            j -= 1
        else:
            i += 1 
    return cnt 