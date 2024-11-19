# You are given a sorted array A of size N and a target value B.
# Your task is to find the index (0-based indexing) of the target value in the array.

# If the target value is present, return its index.
# If the target value is not found, return the index of least element greater than equal to B.
# If the target value is not found and least number greater than equal to target is also not present, return the length of array (i.e. the position where target can be placed)
# Your solution should have a time complexity of O(log(N)).

def searchInsert(A, B):
        s = 0
        e = len(A) - 1
        if A[e] < B:
            ans = len(A)
        while (s <= e):
            mid = (s+e)//2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                s = mid + 1
            else:
                e = mid - 1
                ans = mid
        return ans

print(searchInsert([1,3,5,6],5))
