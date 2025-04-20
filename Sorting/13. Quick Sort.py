# Given an integer array A, sort the array using QuickSort.

def solve(A):
    
    def find_pivot(A,s,e):
        p1 = s + 1
        p2 = e
        ref = A[s]
        while p1 <= p2:
            if A[p1] <= ref:
                p1 += 1
            elif A[p2] > ref:
                p2 -= 1
            else:
                A[p1],A[p2] = A[p2],A[p1]
                p1 += 1
                p2 -= 1
        A[s],A[p2] = A[p2],A[s]
        return p2 
    def quick_sort(A,s,e):
        if s >= e:
            return
        p = find_pivot(A,s,e)
        quick_sort(A,s,p-1)
        quick_sort(A,p+1,e)
    quick_sort(A,0,len(A)-1)
    return A 