
# https://www.geeksforgeeks.org/problems/search-in-a-matrix17201720/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card




def solve(A, B):
    i = 0
    j = len(A[0]) - 1
    n = len(A)
    m = len(A[0])
    while i < n and j >= 0:
        if A[i][j] < B:
            i += 1
        elif A[i][j] > B:
            j -= 1
        else:
            k = 0
            while k < m:
                if A[i][k] == B:
                    return (i+1)*1009 + (k+1)
                else:
                    k += 1
    return -1