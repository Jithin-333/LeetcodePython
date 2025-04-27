class Solution(object):
    def finalValueAfterOperations(self, operations):
        aftervalue=0
        for i in operations:
            if '-' in i:
                aftervalue -= 1
            if '+' in i:
                aftervalue += 1
        return aftervalue


operations = ["X++","++X","--X","X--"]
sol = Solution()
print(sol.finalValueAfterOperations(operations))

