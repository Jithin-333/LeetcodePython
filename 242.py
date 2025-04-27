class Solution(object):
    def isAnagram(self, s, t):
        return s[-1] == t[-1]
s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s,t))