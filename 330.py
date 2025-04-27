class Solution(object):
    def minElement(self, nums):
        def digitsum(n):
            sum = 0
            while (n !=0):
                sum = sum + int(n % 10)
                n = int(n / 10)
            return sum
        res = []
        for i in nums:
            res.append(digitsum(i))
        print(res)
        return min(res)


sol = Solution()
nums = [10,12,13,14]
print(sol.minElement(nums))