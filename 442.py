class Solution(object):
    def findDuplicates(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        res = []
        for k,v in dic.items():
            if v > 1:
                res.append(k)
        return res


sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print(sol.findDuplicates(nums))