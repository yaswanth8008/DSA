# https://leetcode.com/problems/single-number-iii/description/


def singleNumber(nums):
    num = 0
    for i in nums:
        num = num ^ i 
    position = None
    for i in range(32):
        if num >> i & 1 == 1:
            position = i 
            break
    set_num = 0
    unset_num = 0
    for i in range(len(nums)):
        if nums[i] >> position & 1 == 1:
            set_num = set_num ^ nums[i]
        else:
            unset_num = unset_num ^ nums[i]
    return [set_num,unset_num]