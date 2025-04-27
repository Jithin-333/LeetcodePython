class Solution(object):
    def addDigits(self, num):
        num=str(num)
        s=0
        if len(num)==1:
            return int(num)
        else:
            for j in range(len(num)):
                s=0
                for i in num:
                    s += int(i)
                    num = str(s)
        return s
sol = Solution()
num = 4956
print(sol.addDigits(num))
