# The gray code is a binary numeral system where two successive values differ in only one bit.

# Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.

# A gray code sequence must begin with 0.


def grayCode(A):
    if A == 1:
        return [0,1]
    prev_list = grayCode(A-1)
    arr = []
    n = len(prev_list)
    for i in range(n):
        arr.append(prev_list[i])
    for i in range(n-1,-1,-1):
        arr.append(2**(A-1) + prev_list[i])
    return arr 