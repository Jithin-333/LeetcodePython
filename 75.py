class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums


nums = [2,0,2,1,1,0]
sol = Solution()
print(sol.sortColors(nums))
