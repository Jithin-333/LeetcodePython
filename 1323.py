class Solution(object):
    def maximum69Number(self, num):
        ls = str(num)
        ls = ls.replace('6','9',1)
        return int(ls)

sol = Solution()
num = 9669
print(sol.maximum69Number(num))