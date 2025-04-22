class Solution(object):
    def hasSameDigits(self, s):
        def sameDigits(s):
            if len(s) == 2:
                return s[0] == s[1]
            new_s = ""
            for i in range(len(s) - 1):
                num = (int(s[i]) + int(s[i + 1])) % 10
                new_s = new_s + str(num)
            return sameDigits(new_s)
        return sameDigits(s)


sol = Solution()
s = "3902"
print(sol.hasSameDigits(s))
