# Problem Description

# Given string A denoting an infix expression. Convert the infix expression into a postfix expression.


# String A consists of ^, /, *, +, -, (, ) and lowercase English alphabets where lowercase English alphabets are operands and ^, /, *, +, - are operators.

# Find and return the postfix expression of A.

# NOTE:

# ^ has the highest precedence.
# / and * have equal precedence but greater than + and -.
# + and - have equal precedence and lowest precedence among given operators.

def solve(A):
    def precedence(s):
        if s == '+' or s == '-':
            return 1
        if s == '/' or s == '*':
            return 2 
        if s == '^':
            return 3 

    ans = ''
    stack = []

    i = 0
    while i < len(A):
    
        if A[i] == '(':
            i += 1
            stack2 = []
            while A[i] != ')':
            
                if A[i].isalpha():
                    ans += A[i] 
                    i += 1
                else:
                    if len(stack2) == 0:
                        stack2.append(A[i])
                    else:
                        p1 = precedence(A[i])
                        p2 = precedence(stack2[-1])
                        if p1 > p2:
                            stack2.append(A[i])
                        else:
                            while p1 <= p2:
                                ans += stack2[-1]
                                stack2.pop()
                                if len(stack2) != 0:
                                    p2 = precedence(stack2[-1])
                                else:
                                    p2 = 0
                            stack2.append(A[i]) 
                    i += 1
            while len(stack2) > 0:
                ans += stack2[-1]
                stack2.pop()
            i += 1
    
        else:
            if A[i].isalpha():
                ans += A[i] 
                i += 1
            else:
                if len(stack) == 0:
                    stack.append(A[i])
                else:
                    p1 = precedence(A[i])
                    p2 = precedence(stack[-1])
                    if p1 > p2:
                        stack.append(A[i])
                    else:
                        while p1 <= p2:
                            ans += stack[-1]
                            stack.pop()
                            if len(stack) != 0:
                                p2 = precedence(stack[-1])
                            else:
                                p2 = 0
                        stack.append(A[i]) 
                i += 1

    while len(stack) > 0:
        ans += stack[-1]
        stack.pop()
    return ans



# print(solve("x^y/(a*z)+b"))

print(solve("a+b*(c^d-e)^(f+g*h)-i"))