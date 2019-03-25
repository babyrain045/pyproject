
nums= [0,0,0]
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
        if count < judge_val:
            judge_val = count
            res = tem_list
        if sum(tem_list) == target or len(nums) == 3:
            res = tem_list
            break
        elif sum(tem_list) < target:
            l_flag += 1
        else:
            r_flag -= 1
    i += 1
print(sum(res))



