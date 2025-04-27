class Solution(object):
    def clearDigits(self, s):
        j = 0
        s = list(s)
        for i, c in enumerate(s):
            if c.isdigit():
                j -= 1
            else:
                s[j] = s[i]
                j += 1

        return ''.join(s[:j])

sol = Solution()
s = "acb34"
print(sol.clearDigits(s))