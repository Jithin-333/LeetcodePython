class Solution(object):
    def dominantIndex(self, nums):
        nums_or = nums
        nums = sorted(nums)
        lar = nums[-1]
        for i in range(len(nums) - 1):
            if nums[i] * 2 <= lar:
                c = 1
            else:
                c = 0
                break
        if c == 1:
            return nums_or.index(lar)
        else:
            return -1

sol = Solution()
nums = [0,0,0,1]
x = sol.dominantIndex(nums)
print(x)