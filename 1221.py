class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        dic = {'R':'L','L':'R'}
        ls = []
        for i in s:
            if dic[i] in ls:
                ls.remove(dic[i])
            else:
                ls.append(i)
            if not ls:
                count += 1
        return count

sol = Solution()
s = "RLRRRLLRLL"
print(sol.balancedStringSplit(s))