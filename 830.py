class Solution(object):
    def largeGroupPositions(self, s):
        res =[]
        for _ in range(len(s)-1):
            arr = []
            for i in range(len(s)):
                if s[i] == s[i + 1]:
                    arr.append(i)
                    
        return res


sol = Solution()
s = "abcdddeeeeaabbbcd"
print(sol.largeGroupPositions(s))