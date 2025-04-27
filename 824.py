class Solution(object):
    def toGoatLatin(self, sentence):
        sentence = sentence.split()
        res = []
        for i in sentence:
            if i[0] in "aeiouAEIOU":
                i = i + "ma"
                res.append(i)
            else:
                i = i[1:] + i[0] + "ma"
                res.append(i)
        sentence =[]
        for i in range(len(res)):
            for j in range(i+1):
                res[i] = res[i] + 'a'
            sentence.append(res[i])
        return ' '.join(sentence)


sol = Solution()
sentence = "I speak Goat Latin"
print(sol.toGoatLatin(sentence))