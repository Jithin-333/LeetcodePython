class Solution(object):
    def isMonotonic(self, nums):
        f=0
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                pass
            else:
                f += 1
            if f == 1:
                for i in range(len(nums) - 1):
                    if nums[i] >= nums[i + 1]:
                        pass
                    else:
                        return False
        return True

sol=Solution()
nums = [6,5,4,4]
print(sol.isMonotonic(nums))

