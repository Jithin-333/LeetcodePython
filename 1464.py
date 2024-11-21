class Solution(object):
    def maxProduct(self, nums):
        first = max(nums)
        nums.remove(first)
        second = max(nums)
        return (first-1) * (second - 1)
