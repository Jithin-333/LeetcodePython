class Solution(object):
    def xorOperation(self, n, start):
        res = 0
        for i in range(n):
            res = res ^ (start + 2 * i)
        return res
sol = Solution()
n = 5
start = 0
print(sol.xorOperation(n,start))