class Solution(object):
    def judgeSquareSum(self, c):
        if c == 1:
            return True
        for i in range(0, c):
            for j in range(0, c):
                if (i ** 2) + (j ** 2) == c:
                    return True
        return False

sol = Solution()
c = 3
print(sol.judgeSquareSum(c))