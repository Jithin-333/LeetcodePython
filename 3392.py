class Solution(object):
    def countSubarrays(self, nums):
        count = 0
        for i in range(1,len(nums) - 1):
            if nums[i] == (nums[i-1] + nums[i+1]) * 2:
                count += 1
        return count
        
