class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        numsl = list(set(nums1 + nums2 + nums3))
        newl =[]
        for i in numsl:
            f=0
            if i in nums1:
                f+=1
            if i in nums2:
                f+=1
            if i in nums3:
                f+=1
            if f>=2:
                newl.append(i)
        return newl
sol = Solution()
nums1 = [1,2,2]
nums2 = [4,3,3,3]
nums3 = [5]
print(sol.twoOutOfThree(nums1, nums2, nums3))