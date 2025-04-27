class Solution(object):
    def minimumOperations(self, nums):
        if len(nums) == len(set(nums)):
            return 0
        count = 0
        def element_cut(nums, count):
            nums = nums[3:]
            count += 1
            if len(nums) == len(set(nums)):
                return count
            return element_cut(nums,count)
        return element_cut(nums,count)


sol = Solution()
nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
# nums = [6,7,8,9]
print(sol.minimumOperations(nums))