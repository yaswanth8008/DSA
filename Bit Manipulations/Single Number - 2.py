# https://leetcode.com/problems/single-number-ii/




def singleNumber(A):
    imposter = 0
    for i in range(0,32):
        cnt = 0
        for j in range(len(A)):
            if A[j] >> i & 1 == 1:
                cnt += 1
        if cnt % 3 == 1:
            imposter += 2**i 
    return imposter