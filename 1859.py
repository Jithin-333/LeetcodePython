class Solution(object):
    def sortSentence(self, s):
        s=s.split()
        arr=[]
        for i in s:
            x=i[-1]
            i=i.rem
            arr.append(x)
        arr=[int(num) for num in arr]
        print(arr)
        print(s)


sol = Solution()
s = "is2 sentence4 This1 a3"
print(sol.sortSentence(s))