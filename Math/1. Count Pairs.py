# https://www.geeksforgeeks.org/problems/count-pairs-in-array-divisible-by-k/1?itm_source=geeksforgeeks


# Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.



def solve(self, A, B):
    for i in range(len(A)):
        A[i] = A[i]%B
    freq = [0]*(B)
    for i in range(len(A)):
        index = A[i]
        freq[index] += 1
    count = 0
    count += freq[0]*(freq[0]-1)/2
    n = (B//2)+1
    for i in range(1,n):
        j = B - i 
        if i == j:
            count += freq[i]*(freq[i]-1)/2
        else:
            count += freq[i]*freq[j]
    return int(count)%(10**9+7)