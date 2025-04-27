class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        s.reverse()
        s= " ".join(s)
        return s

sol = Solution()
s = "the sky is blue"
print(sol.reverseWords(s))
