class Solution(object):
    def differenceOfSum(self, nums):
        s=sum(nums)
        digit_sum = 0
        for i in nums:
            while i > 0:
                digit_sum += (i % 10)
                i //= 10

        return abs(s-digit_sum)

sol=Solution()
nums = [1,15,6,3]
print(sol.differenceOfSum(nums))