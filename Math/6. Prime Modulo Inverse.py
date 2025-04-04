# Q4. Prime Modulo Inverse

# Given two integers A and B. Find the value of A-1 mod B where B is a prime number and gcd(A, B) = 1.

# A-1 mod B is also known as modular multiplicative inverse of A under modulo B.


def solve(A, B):
    def power(A,B,C):
        if B == 0:
            return 1 
        p = power(A,B//2,C)
        if B%2 == 0:
            return (p*p)%C
        else:
            return (p*p*A)%C
    return power(A,B-2,B)

