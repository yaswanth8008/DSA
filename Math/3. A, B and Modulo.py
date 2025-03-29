

# Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.


def solve(A, B):
    if A - B > 0:
        return A - B 
    else:
        return B - A