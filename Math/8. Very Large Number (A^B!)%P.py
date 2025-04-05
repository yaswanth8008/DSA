


# Given two Integers A, B. You have to calculate (A ^ (B!)) % (1e9 + 7).


def solve(A, B):
    m = 10**9+7
    def fact(n,m):
        f = 1
        for i in range(1,n+1):
            f = (f%m*i%m)%m 
        return f

    def pow(a,b,c):
        if b == 0:
            return 1 
        p = pow(a,b//2,c)
        if b%2 == 0:
            return (p*p)%c 
        else:
            return(a*p*p)%c 
    x = fact(B,m-1)
    return pow(A,x,m)