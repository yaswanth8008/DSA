# Problem Description

# An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.


# Valid operators are +, -, *, /. Each string may be an integer or an operator.

# Note: Reverse Polish Notation is equivalent to Postfix Expression, where operators are written after their operands.

# Example Input

# Input 1:
# A =   ["2", "1", "+", "3", "*"]
# Input 2:
# A = ["4", "13", "5", "/", "+"]


# Example Output

# Output 1:
# 9
# Output 2:
# 6

def evalRPN(A):
    stack = []
    
    for i in A:
        if i not in ["+","-","/","*"]:
            stack.append(int(i))
        else:
            a = stack[-1]
            stack.pop()
            b = stack[-1]
            stack.pop()
            if i == '+':
                stack.append(a+b)
            if i == '-':
                stack.append(b-a)
            if i == '/':
                stack.append(b/a)
            if i == '*':
                stack.append(a*b)
    # print(stack)
    if len(stack) > 1:
            return int(stack[-1]+stack[-2])
    else:
        return int(stack[-1])
    


print(evalRPN(["5","1","2","+","4","*","3","-"]))
