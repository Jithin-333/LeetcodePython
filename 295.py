class Solution(object):
    def isIsomorphic(self, s, t):
        if len(set(s)) != len(set(t)):
            return False
        dic = {key: val for (key,val) in zip (s,t)}

        for i in range(len(s)):
            if dic[s[i]] != t[i]:
                return False
        return True

sol = Solution()
s = "badc"
t = "baba"

print(sol.isIsomorphic(s,t))