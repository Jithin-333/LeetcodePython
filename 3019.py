class Solution(object):
    def countKeyChanges(self, s):
        s = s.lower()
        countKey = 0
        for i in range(1,len(s)):
            if s[i-1] != s[i]:
                countKey += 1
        return countKey
