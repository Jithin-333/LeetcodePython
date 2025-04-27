class Solution(object):
    def singleNumber(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        return dic

sol = Solution()
nums = [2,2,1]
print(sol.singleNumber(nums))