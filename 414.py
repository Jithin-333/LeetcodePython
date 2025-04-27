class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        for _ in range(2):
            nums.remove(max(nums))
        return max(nums)

nums = [2,2,3,1]
sol = Solution()
print(sol.thirdMax(nums))
