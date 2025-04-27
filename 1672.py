class Solution(object):
    def maximumWealth(self, accounts):
        res = 0
        for i in accounts:
            tot = 0
            for j in i:
                tot += j
            if tot > res:
                res = tot
        return res


accounts = [[2,8,7],[7,1,3],[1,9,5]]
sol = Solution()
print(sol.maximumWealth(accounts))