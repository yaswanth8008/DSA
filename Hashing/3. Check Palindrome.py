# Given a string A consisting of lowercase characters.

# Check if characters of the given string can be rearranged to form a palindrome.

# Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

def solve(A):
    d = {}
    for i in A:
        d[i] = d.get(i,0) + 1
    cnt_odd = 0
    for i in d:
        if d[i] % 2 == 1:
            cnt_odd += 1
    if cnt_odd <= 1:
        return 1 
    else:
        return 0