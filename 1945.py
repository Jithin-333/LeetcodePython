import string
class Solution(object):
    def getLucky(self, s, k):
        dic = {key : val for key, val in zip(string.ascii_lowercase, range(1, 27))}
        res = ''
        for i in s:
            if i in dic:
                res += str(dic[i])
        reslt = 0
        for _ in range(k):
            for i in res:
                reslt += int(i)
            res = str(reslt)
            reslt = 0

        return int(res)

s = "iiii"
k = 1
sol = Solution()
print(sol.getLucky(s,k))





