class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        sentence += ' '
        arr = sentence.split()
        for i,word in enumerate(arr):
            if word.startswith(searchWord):
                return i+1
        return -1

sentence = "i love eating burger"
searchWord = "burg"
sol = Solution()
print(sol.isPrefixOfWord(sentence,searchWord))