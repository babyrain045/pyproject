
nums= [-1,2,1,-4]
nums.sort()
target = 1
i = 0
r_flag = len(nums) - 1
res = []
judge_val = abs(max(nums))
while i < len(nums) - 2:
    l_flag = i + 1
    while l_flag < r_flag:
        tem_list = [nums[i], nums[l_flag], nums[r_flag]]
        count = abs(sum(tem_list) - target)
        if count <= judge_val:
            judge_val = count
            res = tem_list
            l_flag += 1
            r_flag -= 1
            while l_flag < r_flag and nums[l_flag] == nums[l_flag - 1]:
                l_flag += 1
            while l_flag < r_flag and nums[r_flag] == nums[r_flag + 1]:
                r_flag -= 1
        elif count > judge_val:
            l_flag += 1
            r_flag -= 1
            while l_flag < r_flag and nums[l_flag] == nums[l_flag - 1]:
                l_flag += 1
            while l_flag < r_flag and nums[r_flag] == nums[r_flag + 1]:
                r_flag -= 1
    while l_flag < r_flag and nums[i] == nums[i - 1]:
        i += 1
        continue
    i += 1
print(res)



