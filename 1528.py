class Solution(object):
    def restoreString(self, s, indices):
        res = ""
        dic = { key:val for key,val in zip(indices,s)}
        for i in range(len(indices)):
            res += dic[i]
        return res


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
sol = Solution()
print(sol.restoreString(s,indices))