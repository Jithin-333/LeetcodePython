class Solution(object):
    def toHex(self, num):
        lis = []
        n = num
        s = 0
        while n != 0:
            s = n % 16
            lis.append(s)
            n = n // 16
        print(lis)


num = -1
sol = Solution()
print(sol.toHex(num))



