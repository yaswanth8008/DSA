# Given an array A of non-negative integers, arrange them such that they form the largest number.

# Note: The result may be very large, so you need to return a string instead of an integer.


def largestNumber(A):
    def comparator(a,b):
        a = str(a)
        b = str(b)

        if int(a + b) > int(b + a):
            return -1
        elif int(a + b) < int(b + a):
            return 1
        else:
            return 0 
    A = sorted(A,key=cmp_to_key(comparator))
    if A[0] == 0:
        return '0'
    return ''.join([str(i) for i in A])