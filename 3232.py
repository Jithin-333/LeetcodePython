class Solution(object):
    def canAliceWin(self, nums):
        s = 0
        d = 0
        for i in nums:
            if i < 10:
                s += i
            else:
                d += i
        if s == d:
            return False
        return True

nums = [1,2,3,4,10]
sol = Solution()
print(sol.canAliceWin(nums))


