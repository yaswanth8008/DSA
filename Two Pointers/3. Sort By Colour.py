# Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue.

def sortColors(A):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] == 0:
            i += 1 
        else:
            if A[j] == 0:
                A[i],A[j] = A[j],A[i]
                j -= 1
                i += 1
            else:
                j -= 1 
    j = 0
    i = len(A) - 1
    while i > j:
        if A[i] == 2:
            i -= 1 
        else:
            if A[j] == 2:
                A[i],A[j] = A[j],A[i]
                j += 1
                i -= 1
            else:
                j += 1 
    
        
    return A