# Q2) a) Given a sorted array find the floor of a given number. Floor - greatest element <= k in array

def find_floor(arr,k):
    s = 0
    e = len(arr)-1
    ans = -10000000
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == k:
            return arr[mid]
        elif arr[mid] > k:
            e = mid - 1
        else:
            s = mid + 1
            ans = arr[mid]
    return ans


print(find_floor([-5,2,3,6,9,10,11,14,18],5))

# b) Given a sorted array find the  ceil of a given number. ceil - smallest element >= k in array

def find_ceil(arr,k):
    s = 0
    e = len(arr)-1
    ans = 10000000
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == k:
            return arr[mid]
        elif arr[mid] > k:
            e = mid - 1
            ans = arr[mid]
        else:
            s = mid + 1
            
    return ans

print(find_ceil([-5,2,3,6,9,10,11,14,18],5))


