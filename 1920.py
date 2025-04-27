class Solution(object):
    def buildArray(self, nums):
        res = []
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        return res

sol = Solution()
nums = [0,2,1,5,3,4]
print(sol.buildArray(nums))