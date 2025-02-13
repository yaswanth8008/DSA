


# Write a function that takes an integer and returns the number of 1 bits present in its binary representation.

def solve(A):
    max_till_i = -1000000000
    cnt = 0
    for i in range(len(A)):
        max_till_i = max(A[i],max_till_i)
        if max_till_i == i:
            cnt += 1
    return cnt