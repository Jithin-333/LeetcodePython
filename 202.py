class Solution(object):
    def isHappy(self, n):
        n = str(n)

        for j in range(32):
            s=0
            for i in n:
                s+=int(i)**2
                n = str(s)
            if s == 1:
                return True
        return False
sol = Solution()
n = 2
print(sol.isHappy(n))

