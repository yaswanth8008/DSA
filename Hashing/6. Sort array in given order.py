# Given two arrays of integers A and B, Sort A in such a way that the relative order among the elements will be the same as those are in B.
# For the elements not present in B, append them at last in sorted order.

# Return the array A after sorting from the above method.

# NOTE: Elements of B are unique.



def solve(A, B):
    d = {}
    for i in B:
        d[i] = d.get(i,0) + 1 
    p = {}
    for i in A:
        p[i] = p.get(i,0) + 1 
    a = []
    for i in d:
        if i in p:
            if p[i] == 1:
                a.append(i)
            else:
                while p[i] > 0:
                    a.append(i)
                    p[i] -= 1 
    b = []
    for i in range(len(A)):
        if A[i] not in d:
            b.append(A[i])
    b.sort()
    a = a + b 
    return a