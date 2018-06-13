target = 9
nums = [2,11,7,15]

class Solution:
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l_flag = 0
        r_flag = -1
        map_nums = dict(zip(range(len(nums)),nums))
        nums_sort = sorted(nums)

        while l_flag + 1 - r_flag <= len(nums_sort):
            if nums_sort[r_flag] + nums_sort[l_flag] > target:
                r_flag -= 1
            elif nums_sort[l_flag] + nums_sort[r_flag] < target:
                l_flag += 1
            else:
                index = [k for k,v in map_nums.items() if v == nums_sort[l_flag] or v == nums_sort[r_flag]]
                return (index)



a = Solution()
b = a.twoSum(nums,target)
print(b)