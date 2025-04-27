class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = [x for x in range(1,n+1) if x % m != 0]
        num2 = [x for x in range(1,n+1) if x % m == 0]
        return sum(num1) - sum(num2)

n = 5
m = 6
sol = Solution()
print(sol.differenceOfSums(n,m))