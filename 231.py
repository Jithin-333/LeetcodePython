import math
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n%2==0:
            n//=2
        return n==1
s=Solution()
n = 536870912
print(s.isPowerOfTwo(n))