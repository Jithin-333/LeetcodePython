class Solution(object):
    def merge(self, nums1, m, nums2, n):
        t = m + n
        nums1 = [x for x in nums1 if x != 0]
        for i in nums2:
            nums1.append(i)
        return nums1
        
        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol = Solution()
print(sol.merge(nums1,m,nums2,n))