class Solution(object):
    def longestPalindrome(self, s):
        dic ={}
        res = 0
        j = 0
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] % 2 == 0:
                res += dic[i]
            else:
                res += dic[i]-1
                j += 1
        if j > 0:
            res += 1
        return res

s = "abccccdd"
sol = Solution()
print(sol.longestPalindrome(s))
