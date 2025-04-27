class Solution(object):
    def getSneakyNumbers(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        res = []
        for i in dic:
            if dic[i] > 1:
                res.append(i)
        return res



sol = Solution()
nums = [0,1,1,0]
print(sol.getSneakyNumbers(nums))