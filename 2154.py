class Solution(object):
    def findFinalValue(self, nums, original):
        if original not in nums:
            return original
        for i in range(len(nums)):
            if original in nums:
                original = original*2
        return original


sol = Solution()
nums = [5,3,6,1,12]
original = 3
print(sol.findFinalValue(nums,original))

