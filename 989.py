class Solution(object):
    def addToArrayForm(self, num, k):
        s = ''
        for i in num:
            s += str(i)
        tot = str(int(s) + k)
        res = []
        for i in tot:
            res += [int(i)]
        return res
sol = Solution()
num = [1, 2, 0, 0]
k = 34
x = sol.addToArrayForm(num, k)
print(x)
