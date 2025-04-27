class Solution(object):
    def countVowelSubstrings(self, word):
        for i in range(len(word)):
            s = word[i::]
            print(s)

sol = Solution()
word = "cuaieuouac"
print(sol.countVowelSubstrings(word))