class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []
        for i in range(1, len(nums) + 1):
            if i in nums:
                pass
            else:
                res.append(i)
        return res
sol = Solution()
nums = [1,1]
print(sol.findDisappearedNumbers(nums))
