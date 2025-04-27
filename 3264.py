class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for _ in range(k):
            nums[nums.index(min(nums))] = min(nums) * multiplier
        return nums

sol = Solution()
nums = [2,1,3,5,6]
k = 5
multiplier = 2
print(sol.getFinalState(nums, k, multiplier))