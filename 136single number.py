class Solution(object):
    def singleNumber(self, nums):
        un = list(set(nums))
        for i in un:
            x = nums.count(i)
            if x <= 1:
                return i

sol = Solution()
nums = [2, 2, 1]
x = sol.singleNumber(nums)
print(x)
