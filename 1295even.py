
class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            i = len(str(i))
            print(i)
            if i % 2 == 0:
                count += 1
        print(count)

sol = Solution()
nums = [555,901,482,1771]
x = sol.findNumbers(nums)

