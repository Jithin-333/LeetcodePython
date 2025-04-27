class Solution(object):
    def subtractProductAndSum(self, n):
        mul = 1
        sum = 0
        for i in str(n):
            sum += int(i)
            mul *= int(i)
        return mul - sum
sol = Solution()
n = 234
print(sol.subtractProductAndSum(n))