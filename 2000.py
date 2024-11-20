class Solution(object):
    def reversePrefix(self, word, ch):
        j = word.index(ch)
        return word[:j+1][::-1] + word[j+1:]
