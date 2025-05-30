class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
sol = Solution()
s = "azxxzy"
print(sol.removeDuplicates(s))
