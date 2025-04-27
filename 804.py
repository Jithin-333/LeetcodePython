import string
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alp = string.ascii_lowercase
        dic={k:v for (k,v) in zip (alp,morse)}
        res = []
        for i in words:
            letter = ''
            for j in i:
                letter = letter + dic[j]
            res.append(letter)
        return len(set(res))



sol = Solution()
words = ['a']
print(sol.uniqueMorseRepresentations(words))