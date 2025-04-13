# Given an array of positive integers A, check and return whether the array elements are consecutive or not.

# NOTE: Try this with O(1) extra space.



def solve(A):
    A.sort()
    for i in range(1,len(A)):
        if A[i] - A[i-1] != 1:
            return 0
    return 1