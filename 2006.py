class Solution(object):
    def countKDifference(self, nums, k):
        sum = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    sum += 1
        return sum


nums = [1, 3]
k = 3
sol = Solution()
print(sol.countKDifference(nums,k))
