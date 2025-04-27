class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        res = []
        for i in words:
            res.append(i.split(separator))
        out = []
        for i in res:
            for j in i:
                out.append(j)
        res = [x for x in out]

        for i in range(len(out)):
            if out[i] == '':
                res.remove(out[i])
        return res


sol = Solution()
# words = ["one.two.three","four.five","six"]
# separator = "."
words = ["$easy$","$problem$"]
separator = "$"
print(sol.splitWordsBySeparator(words,separator))
