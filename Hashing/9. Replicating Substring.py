# Given a string B, find if it is possible to re-order the characters of the string B so that it can be represented as a concatenation of A similar strings.

# Eg: B = aabb and A = 2, then it is possible to re-arrange the string as "abab" which is a concatenation of 2 similar strings "ab".

# If it is possible, return 1, else return -1.



def solve(A, B):
    d = {}
    for i in B:
        d[i] = d.get(i,0) + 1
    for i in d:
        if d[i] % A != 0:
            return -1 
        else:
            continue 
    return 1