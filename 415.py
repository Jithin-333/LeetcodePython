class Solution(object):
    def addStrings(self, num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        return str(num1 + num2)

num1 = "11"
num2 = "123"
sol = Solution()
print(sol.addStrings(num1, num2))