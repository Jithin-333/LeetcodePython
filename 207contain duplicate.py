class Solution(object):
    def containsDuplicate(self, nums):
        num1 = list(set(nums))
        if sorted(num1) == sorted(nums):
            return False
        else:
            return True


sol = Solution()
nums = [1,2,3,4]
# nums = [1,2,3,1]
#nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
x = sol.containsDuplicate(nums)
print(x)