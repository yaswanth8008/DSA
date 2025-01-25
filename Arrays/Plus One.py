    

# https://leetcode.com/problems/plus-one/

def plusOne(digits):
    digits[-1] += 1
    carry_forward = digits[-1]//10
    digits[-1] = digits[-1]%10
    for i in range(len(digits)-2,-1,-1):
        num = digits[i] + carry_forward
        digits[i] = num%10
        carry_forward = num//10
    if carry_forward == 0:
        return digits
    else:
        digits.insert(0,carry_forward)
        return digits
    
print(plusOne([9,9,9,9]))


# If output should not have leading zeroes then :

# Eg : Input = [0,0,0,1,2,3]
#      Output = [1,2,4]

 
# def plusOne(self, A):
#     A[-1] += 1
#     carry_forward = A[-1]//10
#     A[-1] = A[-1]%10
#     for i in range(len(A)-2,-1,-1):
#         num = A[i] + carry_forward
#         A[i] = num%10
#         carry_forward = num//10
#     if carry_forward != 0:
#         A.insert(0,carry_forward)
      # The below code is to find the index where leading zero ends
#     p = 0
#     while p < len(A) - 1:
#         if A[p] != 0:
#             break 
#         else:
#             p += 1
#     return A[p:]
    