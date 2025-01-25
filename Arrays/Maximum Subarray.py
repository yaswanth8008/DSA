

# https://leetcode.com/problems/maximum-subarray/description/

def maxSubArray(nums):
    summ = 0
    max_sum = nums[0]
    for i in range(len(nums)):
        summ += nums[i]
        max_sum = max(max_sum,summ)
        if summ < 0:
            summ = 0
    return max_sum

print(maxSubArray([5,4,-1,7,8]))