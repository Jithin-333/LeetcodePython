class Solution(object):
    def sumCounts(self, nums):
        out = []
        for i in nums:
            out.append(1)
        out.append(len(set(nums)))
        for i in range(len(nums)):
            out.append(len(set(nums)))
            nums.pop(0)
        out.pop(-1)
        



nums = [1,1]
sol = Solution()
print(sol.sumCounts(nums))