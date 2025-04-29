# Given an unsorted integer array A of size N.


# Find the length of the longest set of consecutive elements from array A.



def longestConsecutive(A):
    ans = -10000000
    hash_set = set(A)
    for i in range(len(A)):
        if A[i] - 1 in hash_set:
            continue 
        else:
            cnt = 1
            next_element = A[i] + 1
            while next_element in hash_set:
                cnt += 1
                next_element += 1
            ans = max(cnt,ans)
    return ans