# Given an integer array A of size N. You have to generate it's all subarrays having a size greater than 1.


# Then for each subarray, find Bitwise XOR of its maximum and second maximum element.

# Find and return the maximum value of XOR among all subarrays.



# Approach-1

# def solve(A):
#     def prevGreater(A):
#         stack = []
#         ans = []
#         for i in range(len(A)):
#             if len(stack) == 0:
#                 ans.append(-1)
#                 # stack.append(A[i])
#             else:
#                 if stack[-1] > A[i]:
#                     ans.append(stack[-1])
#                     # stack.append(A[i])
#                 else:
#                         # keep popping till you find an element greter than A[i]
#                     while len(stack) != 0 and stack[-1] <= A[i]:
#                         stack.pop()
#                     if len(stack) == 0:
#                         ans.append(-1)
#                     else:
#                         ans.append(stack[-1])
#             stack.append(A[i])
#         return ans
#     def nextGreater(A):
#         stack = []
#         ans = []
#         for i in range(len(A)-1,-1,-1):
#             if len(stack) == 0:
#                 ans.append(-1)
#                 # stack.append(A[i])
#             else:
#                 if stack[-1]> A[i]:
#                     ans.append(stack[-1])
#                     # stack.append(A[i])
#                 else:
#                     while len(stack) != 0 and stack[-1] <= A[i]:
#                         stack.pop()
#                     if len(stack) == 0:
#                         ans.append(-1)
#                     else:
#                         ans.append(stack[-1])
#             stack.append(A[i])
#         return ans[::-1]
#     left_max = prevGreater(A)
#     right_max = nextGreater(A)
#     max_xor = 0
#     for i in range(len(A)):
#         a = left_max[i]
#         b = right_max[i]
#         if a > 0:
#             max_xor = max(max_xor,a^A[i])
#         if b > 0:
#             max_xor = max(max_xor,b^A[i])
#     return max_xor
    

# Approach-2


def solve(A):
    stack = []
    stack.append(A[0])
    maximum_xor = 0
    for i in range(1,len(A)):
        if stack[-1] > A[i]:
            maximum_xor = max(maximum_xor,stack[-1]^A[i])
            stack.append(A[i])
        else:
            while len(stack) != 0:
                if stack[-1] < A[i]:
                    maximum_xor = max(maximum_xor,stack[-1]^A[i])
                    stack.pop()
                else:
                    maximum_xor = max(maximum_xor,stack[-1]^A[i])
                    stack.append(A[i])
                    break
            if len(stack) == 1:
                if stack[-1] < A[i]:
                    maximum_xor = max(maximum_xor,stack[-1]^A[i])
                    stack.pop()
                else:
                    maximum_xor = max(maximum_xor,stack[-1]^A[i])
                    stack.append(A[i])

            stack.append(A[i])
    
        
    return maximum_xor

A = [8,4,3,2,9,10,11,6,13]
print(solve(A))




