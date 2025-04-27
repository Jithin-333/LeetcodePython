class Solution(object):
    def finalString(self, s):
        res = []
        for i in s:
            if i == 'i':
                res.reverse()
            else:
                res.append(i)
        return ''.join(res)


s = "poiinter"
sol = Solution()
print(sol.finalString(s))