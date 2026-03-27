# Problem Description

# Given an array of integers A.


# A represents a histogram i.e A[i] denotes the height of the ith histogram's bar. Width of each bar is 1.

# Find the area of the largest rectangle formed by the histogram.



def largestRectangleArea(A):

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
        prevSmaller_arr = prevSmaller(A)
        nextSmaller_arr = nextSmaller(A)

        max_area = 0
        for i in range(len(A)):
            a = prevSmaller_arr[i] + 1
            b = nextSmaller_arr[i] - 1 
            if prevSmaller_arr[i] == -1:
                a = 0
            if nextSmaller_arr[i] == -1:
                b = len(A) - 1 
            max_area = max(max_area,(b-a+1)*A[i])
        return max_area        



print(largestRectangleArea([2,1,3,5,4,3,4,6]))
