from collections import Counter
class Solution(object):
    def commonChars(self, words):
        arr=[]
        for i in words[0]:
            if i in words[1] and words[2]:
                arr.append(i)
                words[1].removeprefix(i)
                words[2].removeprefix(i)
        return arr

sol = Solution()
words = ["bella","label","roller"]
print(sol.commonChars(words))
