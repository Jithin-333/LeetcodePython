class Solution(object):
    def countElements(self, nums):
        count = 0
        for i in range(len(nums) - 1):
            if nums[i-1] < nums[i] and nums[i] < nums[i+1]:
                count += 1
            elif nums[i-1] > nums[i] and nums[i] > nums[i+1]:
                count += 1
        return count


sol = Solution()
nums = [-3,3,3,90]
print(sol.countElements(nums))