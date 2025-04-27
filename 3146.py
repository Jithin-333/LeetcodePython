class Solution(object):
    def findPermutationDifference(self, s, t):
        res = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    res += abs(i-j)
                    break
        return res

sol = Solution()
s = "abcde"
t = "edbac"
print(sol.findPermutationDifference(s,t))





