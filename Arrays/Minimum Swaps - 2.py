




def solve(self, A):
    cnt = 0
    for i in range(len(A)):
        while A[i] != i:
            target_index = A[i] 
            A[i],A[target_index] = A[target_index],A[i]
            cnt += 1
    return cnt 