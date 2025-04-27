class Solution:
    def findClosestNumber(self, nums):
        closest = float('inf')
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
        return closest


sol = Solution()
nums = [-4,-2,1,4,8]
print(sol.findClosestNumber(nums))


class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]
        for num in nums:
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest) and num > closest:
                closest = num
        return closest


nums = [-4, -2, 1, 4, 8]
sol = Solution()
print(sol.findClosestNumber(nums))