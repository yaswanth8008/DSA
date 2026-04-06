# Problem Description

# A CPU has N tasks to be performed. It is to be noted that the tasks have to be completed in a specific order to avoid deadlock. 
# In every clock cycle, the CPU can either perform a task or move it to the back of the queue. 
# You are given the current state of the scheduler queue in array A and the required order of the tasks in array B.

# Determine the minimum number of clock cycles to complete all the tasks.



from collections import deque

def solve(A, B):
    q = deque()
    for i in A:
        q.append(i)
    i = 0
    cycles = 0
    while i < len(B):
        while B[i] != q[0]:
            front = q.popleft()
            q.append(front)
            cycles += 1
            
        q.popleft()
        cycles += 1
        i += 1
    return cycles



A = [2, 3, 1, 5, 4]
B = [1, 3, 5, 4, 2]

print(solve(A,B))

