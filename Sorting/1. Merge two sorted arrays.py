# Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.

# Note: A linear time complexity is expected and you should avoid use of any library function.


def merge_sort(a,b):
    m = len(a)
    n = len(b)
    c = [0]*(m+n)
    p1 = 0
    p2 = 0
    p3 = 0
    while p1 < m and p2 < n:
        if a[p1] <= b[p2]:
            c[p3] = a[p1]
            p1 += 1
            p3 += 1
        else:
            c[p3] = b[p2]
            p2 += 1
            p3 += 1 
    while p1 < m:
        c[p3] = a[p1]
        p1 += 1
        p3 += 1
    while p2 < n:
        p2 += 1
        p3 += 1
    return c


print(merge_sort([-5,-1,3,7,10,12,15],[-4,0,2,8,9]))