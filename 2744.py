class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        maxPair = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j][::-1]:
                    maxPair += 1
        return maxPair
