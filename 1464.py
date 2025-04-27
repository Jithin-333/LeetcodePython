class Solution(object):
    def maxProduct(self, nums):
        first = max(nums)
        nums.remove(first)
        second = max(nums)
        return (first-1) * (second - 1)



sol = Solution()
nums = [3,4,5,2]
print(sol.maxProduct(nums))