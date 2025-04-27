class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            goal = goal[1:] + goal[0]
            if goal == s:
                return True
        return False

sol = Solution()
s = "abcde"
goal = "cdeab"
print(sol.rotateString(s, goal))