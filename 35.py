class Solution(object):
    def searchInsert(self, nums, target):
        if target not in nums:
            nums = nums + [target]
            nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                return i

sol = Solution()
nums = [1,3,5,6]
target = 1
print(sol.searchInsert(nums,target))
