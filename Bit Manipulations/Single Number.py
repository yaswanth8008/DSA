

# https://leetcode.com/problems/single-number/description/


def singleNumber(A):
    num = 0
    for i in A:
        num = num ^ i 
    return num