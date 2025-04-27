class Solution(object):
    def minimumCost(self, cost):
        cost = sorted(cost,reverse=True)
        mincost = sum(cost)
        count = 0
        for i in range(len(cost)):
            if count == 2:
                mincost -= cost[i]
                count = 0
            else:
                count += 1
        return mincost

sol = Solution()
cost = [10,5,9,4,1,9,10,2,10,8]
print(sol.minimumCost(cost))