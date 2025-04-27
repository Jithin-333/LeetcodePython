class Solution(object):
    def addBinary(self, a, b):
        sum = bin(int(a,2) + int(b,2))
        return sum[2:]

a = "11"
b = "1"
sol = Solution()
print(sol.addBinary(a,b))