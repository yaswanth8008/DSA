# Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.


# NOTE:


# Each element in the result should appear as many times as it appears in both arrays.
# The result can be in any order.


def solve(A, B):

    d1 = {}
    for i in A:
        d1[i] = d1.get(i,0) + 1
    d2 = {}
    for k in B:
        d2[k] = d2.get(k,0) + 1
    ans = []
    for i in d1:
        if i in d2:
            p = min(d2[i],d1[i])
            while p > 0:
                ans.append(i)
                p -= 1
    return ans