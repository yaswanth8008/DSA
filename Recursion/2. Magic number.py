# Given a number A, check if it is a magic number or not.

# A number is said to be a magic number if the sum of its digits is calculated till a
# single digit recursively by adding the sum of the digits after every addition. 
# If the single digit comes out to be 1, then the number is a magic number.



def solve(A):

    def sum_digits(n):
        if n == 0:
            return 0
        else:
            return n%10 + sum_digits(n//10)
    a = sum_digits(A)
    while a >= 10:
        a = sum_digits(a)
    if a == 1:
        return 1
    else:
        return 0