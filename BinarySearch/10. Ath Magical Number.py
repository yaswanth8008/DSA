
# You are given three positive integers, A, B, and C.

# Any positive integer is magical if divisible by either B or C.

# Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.

# Note: Ensure to prevent integer overflow while calculating.










def solve(A, B, C):
    def gcd(a,b):
        if b == 0:
            return a 
        else:
            return gcd(b,a%b)
    def lcm(a,b):
        return (a*b)//gcd(a,b)
    def cnt_multiples(a,b,k):
        return k//a + k//b - k//lcm(a,b)
    s = min(B,C)
    e = min(B,C)*A 
    while s <= e:
        m = (s+e)//2 
        if cnt_multiples(B,C,m) > A:
            e = m - 1
        elif cnt_multiples(B,C,m) < A:
            s = m + 1
        else:
            if m%B == 0 or m%C == 0:
                return m % (10**9+7)
            else:
                e = m - 1