# Given an array of integers A, find and return the count of divisors of each element of the array.




def solve(A):
    # Constructing prime_factors array 
    n = max(A)+1
    pf_ar = [0]*n
    for i in range(1,n):
        pf_ar[i] = i 
    for i in range(2,n):
        if pf_ar[i] == i:
            for k in range(2*i,n,i):
                if pf_ar[k] > i:
                    pf_ar[k] = i 
    # getting all the prime factors of a number using prime_factors array
    def prime_factors(n):
        d = {}
        while n > 1:
            p = pf_ar[n]
            d[p] = d.get(p,0) + 1
            n = n//p 
        return d 
    cnt_divisors = []
    for i in range(len(A)):
        prime_divisors = prime_factors(A[i])
        cnt = 1
        for i in prime_divisors:
            num_factors = prime_divisors[i]
            cnt = cnt*(num_factors+1)
        cnt_divisors.append(cnt)
    return cnt_divisors
