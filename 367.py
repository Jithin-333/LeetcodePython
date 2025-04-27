import math
class Solution(object):
    def isPerfectSquare(self, num):
        j = int(math.sqrt(num))
        if j * j == num:
            return True
        else:
            return False

sol = Solution()
num = 14
print(sol.isPerfectSquare(num))