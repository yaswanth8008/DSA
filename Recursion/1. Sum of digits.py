# Given a number A, we need to find the sum of its digits using recursion.


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)