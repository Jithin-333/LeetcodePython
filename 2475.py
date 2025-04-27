class Solution(object):
    def unequalTriplets(self, nums):
        count = 0
        for i in range(len(nums)-1):
            out = []
            out.append(nums[i])
            for j in range(i+1,len(nums)):
                if nums[j] > out[-1]:



nums = [4, 4, 2, 4, 3]
sol = Solution()
print(sol.unequalTriplets(nums))


