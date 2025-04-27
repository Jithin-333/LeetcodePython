class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = 0
        res =[]
        for i in nums:
            for j in nums:
                if i > j:
                    count += 1
            res.append(count)
            count = 0
        return res


sol = Solution()
nums = [7,7,7,7]
print(sol.smallerNumbersThanCurrent(nums))