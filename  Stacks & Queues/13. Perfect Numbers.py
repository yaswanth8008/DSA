# Problem Description

# Given an integer A, you have to find the Ath Perfect Number.

# A Perfect Number has the following properties:

# It comprises only 1 and 2.
# The number of digits in a Perfect number is even.
# It is a palindrome number.
# For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.



from collections import deque

def solve(A):
    q = deque()
    q.append('11')
    q.append('22')
    pop = 0
    while pop != A - 1:
        front = q.popleft()
        n = len(front)

        q.append(front[0:n//2]+'11'+front[n//2:])
        q.append(front[0:n//2]+'22'+front[n//2:])
        pop += 1
    return q.popleft()



print(solve(8))