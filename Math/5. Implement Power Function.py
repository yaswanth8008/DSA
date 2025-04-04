

# Implement pow(A, B) % C. In other words, given A, B and C, Find (AB % C).


def pow(self, A, B, C):
    if A == 0:
        return 0
    if B == 0:
        return 1
    p = pow(A,B//2,C)
    if B%2 == 0:
        return (p*p)%C 
    else:
        return (p*p*A)%C