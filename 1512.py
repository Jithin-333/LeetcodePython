class Solution(object):
    def numIdenticalPairs(self, nums):
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    res += 1
        return res


sol = Solution()
nums = [1,2,3]
print(sol.numIdenticalPairs(nums))
