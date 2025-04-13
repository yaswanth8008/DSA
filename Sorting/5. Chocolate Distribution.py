# Given an array A of N integers where the i-th element represent the number of chocolates in the i-th packet.

# There are B number of students, the task is to distribute chocolate packets following below conditions:

# 1. Each student gets one packets.
# 2. The difference between the number of chocolates given to any two students is minimum.
# Return the minimum difference (that can be achieved) between the student who gets minimum number of chocolates 
# and the student who gets maximum number of chocolates.

# Note: If you can't give each student 1 packet, return 0.


def solve(A, B):
    if B == 0:
        return 0
    if B > len(A):
        return 0
    else:
        A.sort()
        min_diff = 10000000
        min_index = -1
        for i in range(len(A)-B+1):
            if A[i+B-1] - A[i] < min_diff:
                min_diff = A[i+B-1] - A[i]
                min_index = i 

        return A[min_index+B-1] - A[min_index] 