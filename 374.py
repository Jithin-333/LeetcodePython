class Solution(object):
    def guessNumber(self, n):
        low,high = 1,n
        while low <= high:
            mid = high + low // 2
            res = guess(mid)
            if res == 0:
                return mid 
            elif res == -1:
                high = mid - 1

            else:
                low = mid + 1

sol = Solution()
n = 10
pick = 6
print(sol.guessNumber(n))
