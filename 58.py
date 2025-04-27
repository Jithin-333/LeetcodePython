class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.split()
        l = len(s)
        d=len(s[l-1])
        return d

s = "Hello World"
sol=Solution()
print(sol.lengthOfLastWord(s))