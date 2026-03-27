# Given a 2D binary matrix of integers A containing 0's and 1's of size N x M.

# Find the largest rectangle containing only 1's and return its area.

# Note: Rows are numbered from top to bottom and columns are numbered from left to right.




# thala pranam thokaku vachindhi
def solve(A):
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



    heights = []
    for j in range(0,len(A[0])):
        ans = []
        stack = []
        for i in range(0,len(A)):
            if A[i][j] == 1 and len(stack) == 0:
                stack.append(1)
                ans.append(1)
            elif A[i][j] == 1:
                a = stack[-1] + 1
                stack.pop()
                stack.append(a)
                ans.append(a)

            else:
                if A[i][j] == 0 and len(stack) == 0:
                    ans.append(0)
                else:
                    stack.pop()
                    ans.append(0)
        heights.append(ans)
    max_Area = 0
    for j in range(0,len(heights[0])):
        l = []
        for i in range(0,len(heights)):
            l.append(heights[i][j])
        # print(l)
        area = largestRectangleArea(l)
        # print(area)
        max_Area = max(max_Area,largestRectangleArea(l))

    # print(heights)

    # print(max_Area)

    return max_Area


A = [[0,0,0,0,0],
    [0,1,1,0,0],
    [0,1,1,1,1],
    [0,0,1,1,1],
    [0,0,1,1,1]]

print(solve(A))