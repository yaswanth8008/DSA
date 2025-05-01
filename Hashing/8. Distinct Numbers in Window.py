# You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.

# Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

# NOTE: if B > N, return an empty array.



def dNums(A, B):
    d = {}
    ans = []
    cnt = 0
    for i in range(B):
        d[A[i]] = d.get(A[i],0) + 1
    ans.append(len(d))

    for i in range(0,len(A)-B):
        d[A[i]] -= 1
        if d[A[i]] == 0:
            d.pop(A[i])
        d[A[i+B]] = d.get(A[i+B],0) + 1
        ans.append(len(d))
    return ans