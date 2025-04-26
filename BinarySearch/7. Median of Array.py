# There are two sorted arrays A and B of sizes N and M respectively.

# Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

# NOTE:

# The overall run time complexity should be O(log(m+n)).
# IF the number of elements in the merged array is even, then the median is the average of (n/2)th and (n/2+1)th element. 
# For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5.


def findMedianSortedArrays(A, B):
    if len(A) > len(B):
        A,B = B,A
    n = len(A)
    m = len(B)
    start = 0
    end = n
    while start <= end:
        cut_1 = (start+end)//2
        cut_2 = (n+m)//2 - cut_1
        if cut_1 != 0:
            l1 = A[cut_1 - 1]
        else:
            l1 = -100000000
        if cut_2 != 0:
            l2 = B[cut_2 - 1]
        else:
            l2 = -100000000
        if cut_1 != n:
            r1 = A[cut_1]
        else:
            r1 = 100000000 
        if cut_2 != m:
            r2 = B[cut_2]
        else:
            r2 = 100000000
        if l1 > r2:
            end = cut_1 - 1
        elif l2 > r1:
            start = cut_1 + 1
    
        else:
            if (n+m)%2 == 0:
                return (max(l1,l2) + min(r1,r2))/2
            else:
                return min(r1,r2)
