# Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.


# NOTE: All the A integers will fit in 32-bit integers.



from collections import deque

def solve(A):
    q = deque()
    nums = []
    q.append("1")
    q.append("2")
    q.append("3")
    pop = 0
    while pop != A:
        front = q.popleft()
        q.append(front+"1")
        q.append(front+"2")
        q.append(front+"3")
        pop += 1
        nums.append(front)
    
    return nums





print(solve(7))