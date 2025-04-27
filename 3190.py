class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        for i in nums:
            if i % 3 == 0:
                pass
            else:
                if (i + 1) % 3 == 0:
                    count += 1
                elif (i - 1) % 3 == 0:
                    count += 1
        return count




sol = Solution()
nums = [3,6,9]
print(sol.minimumOperations(nums))