#Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example,if s = "abcde", then it will be "bcdea" after one shift.
# Example1
# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2
# Input: s = "abcde", goal = "abced"
# Output: false

class Solution(object):
    def rotateString(self, s, goal):
        s = s
        goal = goal
        l = len(s)
        s = list(s)
        for i in range(l):
            s.append(s[0])
            for j in range(l):
                s

        print(s)
            # if str(s) == goal:
            #     print("True")
            #     break
            # else:
            #     print("False")
            #     break

sol = Solution()
sol.rotateString("abcde","cdeab")