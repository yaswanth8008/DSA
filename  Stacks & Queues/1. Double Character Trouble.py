# You have a string, denoted as A.

# To transform the string, you should perform the following operation repeatedly:
# Identify the first occurrence of consecutive identical pairs of characters within the string.
# Remove this pair of identical characters from the string.
# Repeat steps 1 and 2 until there are no more consecutive identical pairs of characters.
# The final result will be the transformed string.



def solve(A):
    stack = []
    ans = ''
    for i in range(len(A)):
        if len(stack) != 0 and A[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(A[i])
    while len(stack) != 0:
        ans = stack[-1] + ans 
        stack.pop()
    return ans