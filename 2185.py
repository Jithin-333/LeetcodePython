class Solution(object):
    def prefixCount(self, words, pref):
        count = 0
        l = len(pref)
        for i in words:
            if i[:l] == pref:
                count += 1
        return count


sol = Solution()
words = ["leetcode","win","loops","success"]
pref = "code"
print(sol.prefixCount(words,pref))