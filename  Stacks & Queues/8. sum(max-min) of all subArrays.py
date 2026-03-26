# Given an array of integers A.


# The value of an array is computed as the difference between the maximum element in the array and the minimum element in the array A.

# Calculate and return the sum of values of all possible subarrays of A modulo 109+7.




def solve(A):
    def prevGreater(A):
        stack = []
        ans = []
        for i in range(len(A)):
            if len(stack) == 0:
                ans.append(-1)
                # stack.append(A[i])
            else:
                if A[stack[-1]] > A[i]:
                    ans.append(stack[-1])
                    # stack.append(A[i])
                else:
                        # keep popping till you find an element greter than A[i]
                    while len(stack) != 0 and A[stack[-1]] <= A[i]:
                        stack.pop()
                    if len(stack) == 0:
                        ans.append(-1)
                    else:
                        ans.append(stack[-1])
            stack.append(i)
        return ans

    def nextGreater(A):
        stack = []
        ans = []
        for i in range(len(A)-1,-1,-1):
            if len(stack) == 0:
                ans.append(-1)
                # stack.append(A[i])
            else:
                if A[stack[-1]] > A[i]:
                    ans.append(stack[-1])
                    # stack.append(A[i])
                else:
                    while len(stack) != 0 and A[stack[-1]] <= A[i]:
                        stack.pop()
                    if len(stack) == 0:
                        ans.append(-1)
                    else:
                        ans.append(stack[-1])
            stack.append(i)
        return ans[::-1]

    def prevSmaller(A):
        stack = []
        ans = []
        for i in range(len(A)):
            if len(stack) == 0:
                ans.append(-1)
                # stack.append(A[i])
            else:
                if A[stack[-1]] < A[i]:
                    ans.append(stack[-1])
                    # stack.append(A[i])
                else:
                    # keep popping till you find an element greter than A[i]
                    while len(stack) != 0 and A[stack[-1]] >= A[i]:
                        stack.pop()
                    if len(stack) == 0:
                        ans.append(-1)
                    else:
                        ans.append(stack[-1])
            stack.append(i)
        return ans

    def nextSmaller(A):
        stack = []
        ans = []
        for i in range(len(A)-1,-1,-1):
            if len(stack) == 0:
                ans.append(-1)
                # stack.append(A[i])
            else:
                if A[stack[-1]] < A[i]:
                    ans.append(stack[-1])
                    # stack.append(A[i])
                else:
                    while len(stack) != 0 and A[stack[-1]] >= A[i]:
                        stack.pop()
                    if len(stack) == 0:
                        ans.append(-1)
                    else:
                        ans.append(stack[-1])
            stack.append(i)
        return ans[::-1]

    indices_prev_greater = prevGreater(A)
    indices_next_greater = nextGreater(A)
    indices_prev_smaller = prevSmaller(A)
    indices_next_smaller = nextSmaller(A)
    max_sum = 0
    for i in range(len(A)):
        a = i - indices_prev_greater[i]
        b = indices_next_greater[i] - i
        if indices_prev_greater[i] == -1:
            a = i + 1
        if indices_next_greater[i] == -1:
            b = len(A) - i 
        max_sum += (a*b*A[i])
    min_sum = 0
    for i in range(len(A)):
        a = i - indices_prev_smaller[i]
        b = indices_next_smaller[i] - i
        if indices_prev_smaller[i] == -1:
            a = i + 1
        if indices_next_smaller[i] == -1:
            b = len(A) - i 
        min_sum += (a*b*A[i])

    return (max_sum-min_sum)%((10**9)+7)


print(solve([4, 7, 3, 8]))




