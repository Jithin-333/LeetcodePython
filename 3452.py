class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        sum = 0
        for i in range(len(nums)):
            is_good = True
            if i - k >= 0:
                if nums[i] <= nums[i-k]:
                    is_good = False
            if i + k < len(nums):
                if nums[i] <= nums[i+k]:
                    is_good = False
            if is_good:
                sum += nums[i]
        return sum
