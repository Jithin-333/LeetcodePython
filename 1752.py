class Solution(object):
    def check(self, nums):
        d_nums = sorted(nums)
        for _ in range(len(nums)):
            j = d_nums.pop(0)
            d_nums.append(j)
            if d_nums == nums:
                return True
        return False


sol = Solution()
nums = [3,4,5,1,2]
print(sol.check(nums))
