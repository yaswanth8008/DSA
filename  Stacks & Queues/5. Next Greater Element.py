# Given an array A, find the next greater element G[i] for every element A[i] in the array.
# The next greater element for an element A[i] is the first greater element on the right side of A[i] in the array, A.


# More formally:

# G[i] for an element A[i] = an element A[j] such that 
#     j is minimum possible AND 
#     j > i AND
#     A[j] > A[i]


def nextGreater(A):
    stack = []
    ans = []
    for i in range(len(A)-1,-1,-1):
        if len(stack) == 0:
            ans.append(-1)
            # stack.append(A[i])
        else:
            if stack[-1] > A[i]:
                ans.append(stack[-1])
                # stack.append(A[i])
            else:
                while len(stack) != 0 and stack[-1] <= A[i]:
                    stack.pop()
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
        stack.append(A[i])
    return ans[::-1]