# Divisor game

# Scooby has 3 three integers A, B, and C.
# Scooby calls a positive integer special if it is divisible by B and it is divisible by C. 
# You need to tell the number of special integers less than or equal to A.


def solve(A, B, C):
    def gcd(a,b):
        if b == 0:
            return a 
        else:
            return gcd(b,a%b)
    
    lcm = abs(B * C) // gcd(B,C)
    cnt = 0
    for i in range(lcm,A+1,lcm):
        cnt += 1
    return cnt