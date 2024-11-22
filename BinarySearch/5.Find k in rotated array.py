def search(A, B):
    def find_k(A):
        s = 0
        e = len(A) - 1
        while s <= e:
            mid = (s+e)//2
            if A[mid] < A[mid-1]:
                return mid 
            elif A[mid] < A[0]:
                e = mid - 1
            elif A[mid] > A[0]:
                s = mid + 1
        return 0
    k = find_k(A)
    if k == 0:
        s = 0
        e = len(A)-1
        while (s<=e):
            mid = (s+e)//2
            if A[mid] == B:
                return mid 
            elif A[mid] > B:
                e = mid - 1
            else:
                s = mid + 1 
    else:
        s = 0
        e = k-1
        while (s<=e):
            mid = (s+e)//2
            if A[mid] == B:
                return mid 
            elif A[mid] > B:
                e = mid - 1
            else:
                s = mid + 1 
        s = k
        e = len(A) - 1
        while (s<=e):
            mid = (s+e)//2
            if A[mid] == B:
                return mid 
            elif A[mid] > B:
                e = mid - 1
            else:
                s = mid + 1 
    return -1

print(search([ 9, 10, 3, 5, 6, 8 ],5))