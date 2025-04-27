class Solution(object):
    def reversePrefix(self, word, ch):
        j = word.index(ch)
        return word[:j+1][::-1] + word[j+1:]


sol = Solution()
word = "abcdefd"
ch = "d"
print(sol.reversePrefix(word,ch))