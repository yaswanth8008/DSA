# Given an integer array, A of size N.
# You have to find all possible non-empty subsequences of the array of numbers and then,
# for each subsequence, find the difference between the largest and smallest number in that subsequence.
# Then add up all the differences to get the number.

# As the number may be large, output the number modulo 1e9 + 7 (1000000007).

# NOTE: Subsequence can be non-contiguous.



def solve(A):
    A.sort()
    p1 = 0
    p2 = len(A) - 1
    p3 = len(A) - 1
    cnt = 0
    while p1 < p3:
        while p1 < p2:
            cnt += (A[p2] - A[p1])*(2**(p2-p1-1))
            p2 -= 1
        p1 += 1 
        p2 = len(A) - 1
    return cnt % (10**9+7)