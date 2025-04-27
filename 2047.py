class Solution(object):
    def countValidWords(self, sentence):
        spec = [' ', '-', '!', '.',  ',']
        sentence = sentence.split()
        count = 0
        for i in sentence:
            for j in spec:
                if j in i:
                    break
                count += 1


        return count



sol = Solution()
sentence = "alice and  bob are playing stone-game10"
print(sol.countValidWords(sentence))