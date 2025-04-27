class Solution(object):
    def strongPasswordCheckerII(self, password):
        if len(password) < 8:
            return False
        for i in password:
            if i 


sol = Solution()
password = "IloveLe3tcode!"
print(sol.strongPasswordCheckerII(password))