class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        res = ""
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                res += s1[i]
        return len(res) == len(s1)-2


sol = Solution()
s1 = 'abcd'
s2 = 'dcba'
print(sol.areAlmostEqual(s1,s2))