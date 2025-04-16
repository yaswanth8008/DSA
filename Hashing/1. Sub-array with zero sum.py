# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

# If the given array contains a sub-array with sum zero return 1, else return 0.



def solve(A):

    pf_arr = [0]*len(A)
    pf_arr[0] = A[0]
    for i in range(1,len(A)):
        pf_arr[i] = pf_arr[i-1] + A[i]
    d = {}
    for i in pf_arr:
        d[i] = d.get(i,0) + 1
    for i in d:
        if d[i] > 1 or i == 0:
            return 1 
    
    return 0