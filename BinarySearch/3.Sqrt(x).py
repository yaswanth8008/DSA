# https://leetcode.com/problems/sqrtx/description/


def sqrt(A):
    s = 0
    e = A 
    while (s <= e):
        mid = (s+e)//2
        if mid*mid == A:
            return mid 
        elif mid*mid > A:
            e = mid - 1
        else:
            s = mid + 1
            ans = mid
    return ans

print(sqrt(24))