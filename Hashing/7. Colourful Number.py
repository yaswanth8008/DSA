# Given a number A, find if it is COLORFUL number or not.

# If number A is a COLORFUL number return 1 else, return 0.

# What is a COLORFUL Number:

# A number can be broken into different consecutive sequence of digits. 
# The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245. 
# This number is a COLORFUL number, since the product of every consecutive sequence of digits is different


def colorful(A):
    A = str(A)
    hast_set = set()
    hast_set.add(int(A[0]))

    for i in range(1,len(A)):
        if int(A[i]) in hast_set or int(A[i]) == 0:
            return 0
        elif int(A[i])*int(A[i-1]) in hast_set:
            return 0
        else:
            hast_set.add(int(A[i]))
            if int(A[i])*int(A[i-1]) in hast_set:
                return 0
            else:
                hast_set.add(int(A[i])*int(A[i-1]))
    return 1