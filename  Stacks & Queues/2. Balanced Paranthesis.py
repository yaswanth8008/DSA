# Problem Description

# Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.

# Refer to the examples for more clarity.



def solve(A):
    stack = []
    stack_updated = False
    for i in range(len(A)):
        if A[i] in ('{','[','('):
            stack.append(A[i])
            stack_updated = True 
        if stack_updated == True:

            if stack[-1] == '{' and A[i] == '}':
                stack.pop()
            elif stack[-1] == '(' and A[i] == ')':
                stack.pop()
            elif stack[-1] == '[' and A[i] == ']':
                stack.pop()
    if stack_updated == True:
        if len(stack) != 0 :
            return 0 
        else:
            return 1
    else:
        return 0