class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    count += 1
        return count

sol = Solution()
jewels = "z"
stones = "ZZ"
print(sol.numJewelsInStones(jewels,stones))