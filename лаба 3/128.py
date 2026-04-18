def longestConsecutive(nums):
    nums_set = set(nums)
    max_len = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_len = 1
            while current_num + 1 in nums_set:
                current_num += 1
                current_len += 1
            if current_len > max_len:
                max_len = current_len
    return max_len