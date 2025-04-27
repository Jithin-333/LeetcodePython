class Solution(object):
    def minOperations(self, nums):
        count_num = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                pass
            else:
                count_num += (nums[i] - nums[i + 1]) + 1
                nums[i+1] += (nums[i] - nums[i + 1]) + 1
        return count_num


sol = Solution()
nums = [1,5,2,4,1]
print(sol.minOperations(nums))
