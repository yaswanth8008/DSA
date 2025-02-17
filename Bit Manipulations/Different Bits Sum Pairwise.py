

# https://www.interviewbit.com/problems/different-bits-sum-pairwise/

def cntBits(A):
    n = len(A)
    # cnt = no.of set bits
    f_sum = 0
    for i in range(32):
        cnt = 0
        for j in range(n):
            if A[j] >> i & 1 == 1:
                cnt += 1
        f_sum += (n-cnt)*cnt 
    return (f_sum*2)%(10**9+7)