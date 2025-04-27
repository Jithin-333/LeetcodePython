
class Solution(object):
    def reorderSpaces(self, text):
        count = 0
        word = text.split()
        splen = len(word)-1
        for i in text:
            if i == ' ':
                count += 1
        num = count//splen
        numbal = count - (num * splen)
        res = ''
        for i in word:
            res += i
            for _ in range(num):
                res += ' '
        res = res.strip()
        if numbal:
            for _ in range(numbal):
                res = res + ' '
        return res

sol = Solution()
text = '  this   is  a sentence '
print(sol.reorderSpaces(text))
