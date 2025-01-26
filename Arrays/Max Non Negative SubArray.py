

# https://www.interviewbit.com/problems/max-non-negative-subarray/

def maxset(A):
    curr_sum = 0
    max_sum = 0
    d = []
    left = 0
    right = 0
    for i in range(len(A)):
        
        curr_sum += A[i]
        if curr_sum >= max_sum:
            max_sum = curr_sum
            right = i
        if (curr_sum < max_sum) or (i == len(A)-1):
            indices_list = [0,0,0]
            indices_list[0] = left
            indices_list[1] = right 
            indices_list[2] = max_sum
            left = i + 1
            right = i + 1
            curr_sum = 0
            max_sum = 0
            d.append(indices_list)
    max_sum = 0
    for i in d:
        max_sum = max(max_sum,i[2])
    max_length = 0
    for i in d:
        if i[2] == max_sum:
            length = i[2] - i[1] + 1
            i[2] = length
            max_length = max(length,max_length)

    if max_length == 1:
        return [0]

    for i in d:
        if i[2] == max_length:
            return A[i[0]:i[1]+1]
   
