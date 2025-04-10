# Write a recursive function that takes a string, S, as input and prints the characters of S in reverse order.


def print_reverse(s):
    if len(s) == 1:
        return s 
    else:
        return s[-1] + print_reverse(s[0:-1])