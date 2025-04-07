# You are given two positive numbers A and B . You need to find the maximum valued integer X such that:

# X divides A i.e. A % X = 0
# X and B are co-prime i.e. gcd(X, B) = 1



def cpFact(A, B):
    def gcd(a,b):
        if b == 0:
            return a 
        else:
            return gcd(b,a%b)
    if A == B:
        return 1
    else:
        while gcd(A,B) != 1:
            A = A//gcd(A,B)
        return A