class Solution(object):
    def addedInteger(self, nums1, nums2):
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        out = nums2[0] - nums1[0]
        return out

sol = Solution()
nums1 = [10]
nums2 = [5]
print(sol.addedInteger(nums1, nums2))

