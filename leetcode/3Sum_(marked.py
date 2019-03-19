
class Solution:
    def three_sum(self,num):
        num.sort()
        res = []
        i = 0
        while i < len(num) - 2:
            left = i+1
            right = len(num) - 1
            while left < right:
                elem = [num[i],num[left],num[right]]
                equ = sum(elem)
                if equ == 0:
                    res.append(elem)
                    left += 1
                    right -= 1
                    while left < right and num[left] == num[left-1]:
                        left += 1
                    while left < right and num[right] == num[right+1]:
                        right -= 1
                elif equ > 0:
                    right -= 1
                else:
                    left += 1
            i += 1
            while i < len(num) - 2 and num[i] == num[i-1]:
                i += 1
        return res
a = [-1, 0, 1, 2, -1, -4]
b = Solution().three_sum(a)
print(b)


