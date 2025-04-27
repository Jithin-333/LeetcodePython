class Solution(object):
    def countPrefixes(self, words, s):
        s=list(s)
        count = 0
        for i in s:
            if i in words:
                count += 1
        return count


sol = Solution()
words = ["a","b","c","ab","bc","abc"]
s = "abc"
print(sol.countPrefixes(words,s))