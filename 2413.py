class Solution(object):
    def smallestEvenMultiple(self, n):
        if n % 2 == 0:
            return n
        return n * 2

sol = Solution()
n = 6
print(sol.smallestEvenMultiple(n))