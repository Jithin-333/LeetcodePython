class Solution(object):
    def findWordsContaining(self, words, x):
        outArr = []
        for i in range(len(words)):
            if x in words[i]:
                outArr.append(i)
        return outArr
