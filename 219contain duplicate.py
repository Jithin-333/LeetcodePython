class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        num_dict = {}
        for i, num in enumerate(nums):
            if num in num_dict and i - num_dict[num] <= k:
                return True
            num_dict[num] = i
        return False


sol = Solution()
x = sol.containsNearbyDuplicate([1, 0, 1, 1], 1)
print(x)
