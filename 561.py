class Solution(object):
    def arrayPairSum(self, nums):
        nums = sorted((nums))
        res = 0
        i =0
        while i <= len(nums)-1:
            j = i+1
            res += min(nums[i], nums[j])
            i += 2
        return res

sol = Solution()
nums = [1,4,3,2]
print(sol.arrayPairSum(nums))
