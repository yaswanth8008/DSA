# Given an array of integers A, find and return the peak element in it.
# An array element is considered a peak if it is not smaller than its neighbors. For corner elements, we need to consider only one neighbor.

# NOTE:

# It is guaranteed that the array contains only a single peak element.
# Users are expected to solve this in O(log(N)) time. The array may contain duplicate elements.\

def solve(A):
    if len(A) == 1:
        return A[0]
    if A[0] > A[1]:
        return A[0]
    if A[-1] > A[-2]:
        return A[-1]
    
    s = 1
    e = len(A) - 2
    while s <= e:
        mid = (s+e)//2
        if A[mid] >= A[mid+1] and A[mid] >= A[mid-1]:
            return A[mid]
        elif A[mid] > A[mid+1]:
            e = mid - 1
        elif A[mid] > A[mid-1]:
            s = mid + 1

print(solve([1,2,3,4,5,15,12,10,8,7]))