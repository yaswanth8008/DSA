# Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in a 2-D Cartesian plane.

# Find and return the number of unordered quadruplet (i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l]) 
# form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis.


def solve(A, B):
    cnt = 0
    h = set()
    for i in range(len(A)):
        s = str(A[i])+'#'+str(B[i])
        h.add(s)
    
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            point_1 = A[i],B[i]
            point_2 = A[j],B[j]
            # if A[i] == A[j] or B[i] == B[j]:
            #     break
            # else:
            point_3 = A[j],B[i]
            point_4 = A[i],B[j]
            point_3_str =  str(A[j])+'#'+str(B[i])
            point_4_str =  str(A[i])+'#'+str(B[j])
            if point_3_str in h and point_4_str in h:
                cnt += 1
    return cnt//2