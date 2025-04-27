class Solution(object):
    def climbStairs(self, n):
        memo = {1:1,2:2}
        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = f(n-2) + f(n-1)
                return memo[n]
        return f(n)

sol = Solution()
n = 5
print(sol.climbStairs(n))