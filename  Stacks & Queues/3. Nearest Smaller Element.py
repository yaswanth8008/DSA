# Given an array A, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
# More formally,
# G[i] for an element A[i] = an element A[j] such that
# j is maximum possible AND
# j < i AND
# A[j] < A[i]
# Elements for which no smaller element exist, consider the next smaller element as -1.

# or simply

# given an array of positive integers , for every i find nearest element on the left side which is smaller than A[i]

def prevSmaller(A):
    stack = []
    ans = []
    for i in range(len(A)):
        if len(stack) == 0:
            ans.append(-1)
            # stack.append(A[i])
        else:
            if stack[-1] < A[i]:
                ans.append(stack[-1])
                # stack.append(A[i])
            else:
                while len(stack) != 0 and stack[-1] >= A[i]:
                    stack.pop()
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
        stack.append(A[i])
    return ans