

# https://www.interviewbit.com/problems/rearrange-array/


def arrange(A):
    n = len(A)
    for i in range(len(A)):
        A[i] = A[i]*n 
    for i in range(len(A)):
        #A[i] = A[A[i]]
        index = A[i]//n
        new_value = A[index]//n
        A[i] += new_value
    for i in range(len(A)):
        A[i] = A[i]%n 
    return A 
