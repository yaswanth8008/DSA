# Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)], 
# if we split the array into some number of "chunks" (partitions), and individually sort each chunk. 
# After concatenating them in order of splitting, the result equals the sorted array.

# What is the most number of chunks we could have made?


def solve(A):
    max_till_i = -1000000000
    cnt = 0
    for i in range(len(A)):
        max_till_i = max(A[i],max_till_i)
        if max_till_i == i:
            cnt += 1
    return cnt