class Solution(object):
    def intersect(self, nums1, nums2):
        arr = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                arr.append(nums1[i])
                nums2.remove(nums1[i])

        return arr


s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersect(nums1, nums2))
