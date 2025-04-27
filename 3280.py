class Solution(object):
    def convertDateToBinary(self, date):
        date = date.split('-')
        date = [int(x) for x in date]
        res = []
        for i in date:
            res.append(bin(i)[2::])
        res = '-'.join(res)
        return res

sol = Solution()
date = "2080-02-29"
print(sol.convertDateToBinary(date))