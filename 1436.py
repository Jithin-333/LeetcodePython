class Solution(object):
    def destCity(self, paths):
        dic={}
        for i in paths:
            dic[i[0]] = i[1]
        res = ""
        for i in dic:
            if dic[i] in dic:
                pass
            else:
                res += dic[i]
        return res

sol = Solution()
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(sol.destCity(paths))