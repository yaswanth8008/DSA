# A lucky number is a number that has exactly 2 distinct prime divisors.
# You are given a number A, and you need to determine the count of lucky numbers between the range 1 to A (both inclusive).





def solve(A):
    n = A+1
    pf_ar = [0]*n
    for i in range(1,n):
        pf_ar[i] = i 
    pf_ar1 = [0]*n
    for i in range(2,n):
        if pf_ar[i] == i:
            for k in range(2*i,n,i):
                pf_ar[k] = i
                pf_ar1[k] += 1
    cnt = 0
    for i in range(1,n):
        if pf_ar1[i] == 2:
            cnt += 1
    return cnt

solve(21)