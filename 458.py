class Solution(object):
    def repeatedSubstringPattern(self, s):
        dic={x: None for x in s}
        u = [i for i in dic]
        st = ""
        for i in u:
            st += i
        n = int(len(s)) // len(u)
        res = ""
        for _ in range(n):
            res += st
        return res == s

sol = Solution()
s = "abcdabcdabcdabcd"
print(sol.repeatedSubstringPattern(s))

class Solution(object):
    def repeatedSubstringPattern(self, s):
        new_s = (s + s)[1:-1]
        print(new_s)
        return s in new_s

sol = Solution()
s = "abcabcabcabc"
print(sol.repeatedSubstringPattern(s))
