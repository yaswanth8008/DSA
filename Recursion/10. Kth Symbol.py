
# On the first row, we write a 0. Now in every subsequent row, we look at the previous row 
# and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 1-indexed.).








def solve(A, B):
    def find_k(row):
        if row == 1:
            return [0]
        if row == 2:
            return [0,1]
        prev_list = find_k(row - 1)
        arr = []
        n = len(prev_list)
        for i in range(n):
            arr.append(prev_list[i])
        if row % 2 == 0:
            for i in range(n-1,-1,-1):
                arr.append(1-prev_list[i])
        else:
            for i in range(n-1,-1,-1):
                arr.append(prev_list[i])
        return arr
    ans = find_k(A)
    return ans[B-1]