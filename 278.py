def isBadVersion(version):
    bad = 4
    if version < bad:
        return False
    else:
        return True
class Solution(object):
    def firstBadVersion(self, n):
        left,right = 1,n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

sol = Solution()
n = 5
print(sol.firstBadVersion(n))