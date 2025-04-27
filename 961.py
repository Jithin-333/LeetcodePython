class Solution(object):
    def repeatedNTimes(self, nums):
        dic={}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] == len(nums)//2:
                return i

sol = Solution()
nums = [5,1,5,2,5,3,5,4]
print(sol.repeatedNTimes(nums))
