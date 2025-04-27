class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        num = result = 0

        for i in nums:
            if i == 1:
                result += 1
                num = max(num, result)
            else:
                result = 0
        return num



sol = Solution()
nums = [1,1,0,1,1,1]
print(sol.findMaxConsecutiveOnes(nums))
