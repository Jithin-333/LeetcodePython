class Solution(object):
    def shuffle(self, nums, n):
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res


nums = [2, 5, 1, 3, 4, 7]
n = 3
sol = Solution()
print(sol.shuffle(nums,n))