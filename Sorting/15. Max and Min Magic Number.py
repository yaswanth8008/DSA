# Given an array of integers A of size N where N is even.

# Divide the array into two subsets such that

# 1.Length of both subset is equal.
# 2.Each element of A occurs in exactly one of these subset.
# Magic number = sum of absolute difference of corresponding elements of subset.

# Note: You can reorder the position of elements within the subset to find the value of the magic number.

# For Ex:- 
# subset 1 = {1, 5, 1}, 
# subset 2 = {1, 7, 11}
# Magic number = abs(1 - 1) + abs(5 - 7) + abs(1 - 11) = 12
# Return an array B of size 2, where B[0] = maximum possible value of Magic number modulo 109 + 7,
# B[1] = minimum possible value of a Magic number modulo 109 + 7.


def solve(A):
    A.sort()
    
    max_magic_num = 0
    min_magic_num = 0
    i = 0
    j = len(A) - 1
    while i < j:
        max_magic_num += abs(A[j] - A[i])
        i += 1
        j -= 1
    i = 0
    while i < len(A)-1:
        min_magic_num += abs(A[i]-A[i+1])
        i += 2 
    max_magic_num = max_magic_num %(10**9+7)
    min_magic_num = min_magic_num %(10**9+7)
    return [max_magic_num,min_magic_num]