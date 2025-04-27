class Solution(object):
    def findLUSlength(self, a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1

        if count == 0:
            return -1
        else:
            return count

sol = Solution()
a = "aba"
b = "cdc"
print(sol.findLUSlength(a, b))