




def solve(A, B):
    window_size = 0
    swaps = 0
    for i in range(len(A)):
        if A[i] <= B:
            window_size += 1
    cnt = 0    
    for i in range(window_size):
        if A[i] > B:
            cnt += 1
    i = 0
    j = window_size
    new_cnt = cnt
    while j < len(A):
        if A[i] > B:
            cnt -= 1
        if A[j] > B:
            cnt += 1
        new_cnt = min(new_cnt,cnt)
        i += 1
        j += 1
    return new_cnt
