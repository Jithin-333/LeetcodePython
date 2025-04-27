class Solution(object):
    def numberOfMatches(self, n):
        res = 0
        while n > 1:
            if n % 2 == 0:
                match = n // 2
                res += match
                n -= match
            else:
                match = n // 2
                res += match
                n -= match
        return res

sol = Solution()
n = 7
print(sol.numberOfMatches(n))