class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        for i in banned:
            paragraph = paragraph.replace(i,'')
    
        ls = paragraph.split()
        dic={}
        for i in ls:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        res = ''
        j=0
        for i in dic:
            if dic[i] > j:
                j = dic[i]
                res = i
        return res.lower()

sol = Solution()
paragraph = 'Bob'
banned = []
print(sol.mostCommonWord(paragraph,banned))
