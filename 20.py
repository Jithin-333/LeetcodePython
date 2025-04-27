class Solution(object):
    def isValid(self, s):
        st = ['(', ')', '{', '}', '[', ']']
        for i in st:
            if i in s:

                print(i)
         

s = "()[]{}"
sol = Solution()
print(sol.isValid(s))
