class Solution(object):
    def semiOrderedPermutation(self, nums):
        last = len(nums)
        count = 0
        j = nums.index(1)
        while (j > 0):
            nums[j],nums[j-1] = nums[j-1],nums[j]
            j = j - 1
            count += 1

        x = nums.index(last)
        for i in range(x,last - 1):
            nums[i],nums[i+1] = nums[i+1],nums[i]
            count += 1
        return count




nums = [1,2,3,4]
sol = Solution()
print(sol.semiOrderedPermutation(nums))
