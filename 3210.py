class Solution(object):
    def getEncryptedString(self, s, k):
        new=''

        for c in range(len(s)):
            new = new + s[(c+k) % len(s)]

        return new


sol = Solution()
s = "dart"
k = 3
print(sol.getEncryptedString(s,k))