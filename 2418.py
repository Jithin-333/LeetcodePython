class Solution(object):
    def sortPeople(self, names, heights):
        s = sorted(heights)
        a=[]
        myDict = { k:v for (k,v) in zip(heights, names)}
        dictsort = sorted(myDict.keys(), reverse=True)
        for i in dictsort:
            a.append(myDict[i])
        return a

sol = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sol.sortPeople(names,heights))