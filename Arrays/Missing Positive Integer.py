



# https://leetcode.com/problems/first-missing-positive/description/

def firstMissingPositive(A):
    n = len(A)
    for i in range(n):
        while A[i] < n and A[i] >= 0 and (A[i] != i+1):
            target_index = A[i] - 1
            if A[i] == A[target_index]:
                break
            A[i],A[target_index] = A[target_index],A[i]
    for i in range(n):
        if A[i] != i + 1:
            return i + 1
    return n + 1