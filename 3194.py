class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        n = len(nums)
        i = 0
        avg = 0
        while (i < n/2):
            avg = (nums[i] + nums[n-i-1])/ 2
            i = i+1
        return avg

sol = Solution()
nums = [1,2,3,7,8,9]
print(sol.minimumAverage(nums))
