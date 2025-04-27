class Solution(object):
    def largestOddNumber(self, num):
        res = []
        for i in range(1,len(num)+1):
            if res == []:
                if int(num[-i]) % 2 != 0:
                    res.append(num[-i])
            else:
                res.append(num[-i])
        res.reverse()
        return ''.join(res)



sol = Solution()
num = "4206"
print(sol.largestOddNumber(num))