class Solution(object):
    def repeatedCharacter(self, s):
        stack =[]
        for i in s:
            if i in stack:
                return i
            stack.append(i)



s = "abcdd"
sol = Solution()
print(sol.repeatedCharacter(s))