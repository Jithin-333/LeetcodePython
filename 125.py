import string
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        small = string.ascii_lowercase
        num = '1234567890'

        res = ''
        for i in s:
            if i in small or i in num:
                res = res + i
        return res == res[::-1]


sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))