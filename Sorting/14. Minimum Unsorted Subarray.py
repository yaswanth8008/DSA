# Given an array A of non-negative integers of size N. Find the minimum sub-array
# Al, Al+1 ,..., Ar such that if we sort(in ascending order) that sub-array, then the whole array should get sorted.
# If A is already sorted, output -1.




def subUnsort(A):
    B = sorted(A)
    p1 = 0
    p2 = len(A)-1
    while p1 < p2:
        if A[p1] == B[p1]:
            p1 += 1
        elif A[p2] == B[p2]:
            p2 -= 1
        else:
            return [p1,p2]
    return [-1]

