class Solution(object):
    def moveZeroes(self, nums):
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        return nums


sol = Solution()
nums = [0, 1, 0, 3, 12]
x = sol.moveZeroes(nums)
print(x)