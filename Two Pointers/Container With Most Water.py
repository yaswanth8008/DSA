
# https://leetcode.com/problems/container-with-most-water/description/

def maxArea(A):
    i = 0
    j = len(A) - 1
    max_area = -1000000
    while i <= j:
        width = j - i 
        height = min(A[i],A[j])
        area = width*height
        max_area = max(max_area,area)
        if A[i] < A[j]:
            i += 1
        else:
            j -= 1 
    return max_area 


print(maxArea([1,8,6,2,5,4,8,3,7]))