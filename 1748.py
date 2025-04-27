class Solution(object):
    def sumOfUnique(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        res = 0
        for i in dic:
            if dic[i] == 1:
                res += i
        return res


nums = [1, 2, 3, 2]
sol = Solution()
print(sol.sumOfUnique(nums))

