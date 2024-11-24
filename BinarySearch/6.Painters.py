def solve(A,B,C):
    C = [B*i for i in C]
    def is_possible(arr,k,time):
        summ = 0
        workers = 0
        for i in range(len(arr)):
            summ += arr[i]
            if summ > time:
                workers += 1
                summ = arr[i]
                if workers == k:
                    return False
        return True
    def min_time(arr,k):
        
        s = max(arr) # maximum time.If only one element is in array that is the maximum time
        e = sum(arr) # sum of all elements.If #workers = 1 then sum
        while (s <= e):
            mid = (s+e)//2
            if is_possible(arr,k,mid):
                e = mid - 1
                ans = mid
            else:
                s = mid + 1
        return ans
    return min_time(C,A)

print(solve(10,1,[1,8,11,3]))
 
    
        
    