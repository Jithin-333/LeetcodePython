class Solution(object):
    def mergeAlternately(self, word1, word2):
        arr=""
        s=0
        if len(word1) < len(word2):
            sm = word1
        else:
            sm = word2

        if len(word1) > len(word2):
            lg = word1
        else:
            lg = word2

        for i in range(len(sm)):
            arr = arr + word1[i] + word2[i]
        s = len(lg)-len(sm)
        for i in range(s):
            arr = arr + lg[s+i]

        return arr



s=Solution()
word1 = "ab"
word2 = "pqrs"
print(s.mergeAlternately(word1,word2))
