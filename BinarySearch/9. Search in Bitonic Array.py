# Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

# NOTE:

# A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.


def solve(A, B):
    def find_pivot(arr):
        s = 0
        e = len(arr) - 1
        m = (s+e)//2
        while s <= e:
            m = (s+e)//2
            if arr[m - 1] < arr[m] and arr[m] > arr[m + 1]:
                return m
            if arr[m - 1] < arr[m]:
                s = m + 1
            else:
                e = m - 1
            
    k = find_pivot(A)
    s = 0
    e = k
    while s <= e:
        m = (s+e)//2
        if A[m] == B:
            return m 
        elif A[m] < B:
            s = m + 1
        else:
            e = m - 1
    s = k + 1
    e = len(A) - 1
    while s <= e:
        m = (s+e)//2
        if A[m] == B:
            return m 
        elif A[m] < B:
            e = m - 1
        else:
            s = m + 1
    return -1