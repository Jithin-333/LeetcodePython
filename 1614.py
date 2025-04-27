class Solution(object):
    def maxDepth(self, s):
        s = [x for x in s if x == '(' or x == ')']
        par = {'(':')'}
        stack = []
        for i in s:
            if par[i] in stack:
                



s = "(1+(2*3)+((8)/4))+1"
sol = Solution()
print(sol.maxDepth(s))