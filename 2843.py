class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0
        for i in range(low, 10):
            i = str(i)
            print(i)

sol = Solution()
low = 1
high = 100
print(sol.countSymmetricIntegers(low,high))