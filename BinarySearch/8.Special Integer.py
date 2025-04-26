# Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with the sum of elements greater than B.



def solve(A, B):
    def check(arr,k,B):
        # This array checks if there is any sub-array of size k whose sum <= B exists
        n = len(arr)
        summ = 0
        cnt = 0
        for i in range(k):
            summ += arr[i]
        if summ <= B:
            cnt += 1
        for s in range(1,n - k + 1):
            summ -= arr[s-1]
            summ += arr[s+k-1]
            if summ <= B:
                cnt += 1 
        if cnt == n - k + 1:
            return True
        else:
            return False 
    ans = None
    k_min = 0
    k_max = len(A)
    while k_min <= k_max:
        mid = (k_min + k_max)//2
        if check(A,mid,B):
            ans = mid 
            k_min = mid + 1
        else:
            k_max = mid - 1
    return ans
    