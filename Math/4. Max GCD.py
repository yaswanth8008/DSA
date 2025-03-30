

# https://www.geeksforgeeks.org/remove-an-element-to-maximize-the-gcd-of-the-given-array/


def solve(A):
    def gcd(a,b):
        if b == 0:
            return a 
        else:
            return gcd(b,a%b)
    n = len(A)
    pf_gcd = [0]*n
    pf_gcd[0] = A[0]
    for i in range(1,n):
        pf_gcd[i] = gcd(pf_gcd[i-1],A[i])
    sf_gcd = [0]*n
    sf_gcd[-1] = A[-1]
    for i in range(n-2,-1,-1):
        sf_gcd[i] = gcd(sf_gcd[i+1],A[i])
    max_gcd = max(pf_gcd[n-2],sf_gcd[1])
    for i in range(1,n-1):
        left = pf_gcd[i-1]
        right = sf_gcd[i+1]
        max_gcd = max(max_gcd,gcd(left,right))
    return max_gcd
