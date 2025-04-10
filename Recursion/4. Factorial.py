# Write a program to find the factorial of the given number A using recursion.

# Note: The factorial of a number N is defined as the product of the numbers from 1 to N.


def factorial(A):
    if A == 0 or A == 1:
        return 1
    else:
        return A*factorial(A-1)