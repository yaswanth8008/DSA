# Given an array of integers A, we call (i, j) an important reverse pair if i < j and A[i] > 2*A[j].
# Return the number of important reverse pairs in the given array A.



def solve(A):
    def merge_inversions(arr,s,e,m):
        p1 = s 
        p2 = m+1
        cnt = 0
        while p1 <= m and p2 <= e:
            if arr[p1] <= 2 * arr[p2]:
                p1 += 1
            else:
                cnt += m - p1 + 1
                p2 += 1
        p1 = s 
        p2 = m+1
        p3 = 0
        c = [0]*(e-s+1)
        while p1 <= m and p2 <= e:
            if arr[p1] <= arr[p2]:
                c[p3] = arr[p1]
                p1 += 1
                p3 += 1
        
            else:
                c[p3] = arr[p2]
                p2 += 1
                p3 += 1
        while p1 <= m:
            c[p3] = arr[p1]
            p1 += 1
            p3 += 1
        while p2 <= e:
            c[p3] = arr[p2]
            p2 += 1
            p3 += 1
        for i in range(len(c)):
            arr[i+s] = c[i]
        return cnt
    
    
    def inversion_count(arr,s,e):
        if s == e:
            return 0
        m = (s+e)//2
        left = inversion_count(arr,s,m)
        right = inversion_count(arr,m+1,e)
        merged = merge_inversions(arr,s,e,m)
        return left + right + merged 
    start = 0
    end = len(A) - 1
    ans = inversion_count(A,start,end)
    return ans