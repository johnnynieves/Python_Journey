def find_max(nums):
    high_num = 0
    for i in nums:
        if i > high_num:
            high_num = i
    return high_num
