class Solution(object):
    def findDifference(self, nums1, nums2):
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nm1 = [x for x in nums1]
        nm2 = [x for x in nums2]
        for i in nums1:
            if i in nums2:
                nm1.remove(i)
                nm2.remove(i)
        return [nm1, nm2]
