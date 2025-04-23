# Shaggy has an array A consisting of N elements. 
# We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.


# Shaggy wants you to find a special pair such that the distance between that pair is minimum. 
# Distance between two indices is defined as |i-j|. 
# If there is no special pair in the array, then return -1.


def solve(A):
    d = {}
    min_dist = 100000000
    for i in range(len(A)):
        if A[i] not in d:
            d[A[i]] = i 
        else:
            min_dist = min(min_dist,i - d[A[i]])
            d[A[i]] = i 
    if min_dist == 100000000:
        return -1
    else:
        return min_dist