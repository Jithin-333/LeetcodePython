class Solution(object):
    def countKDifference(self, nums, k):
        sum = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    sum += 1
        return sum
