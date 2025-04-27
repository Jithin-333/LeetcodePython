# class Solution(object):
#     def intersection(self, nums1, nums2):
#         arr=[]
#         for i in nums1:
#             for j in nums2:
#                 if i == j:
#                     arr.append(j)
#         arr=list(set(arr))
#         return arr
#
# s=Solution()
# nums1 = [9,4,9,8,4]
# nums2 = [4,9,5]
# print(s.intersection(nums1,nums2))

class Solution(object):
    def intersection(self, nums1, nums2):
        arr=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                arr.append(nums1[i])
        arr=list(set(arr))
        return arr

s=Solution()
nums1 = [9,4,9,8,4]
nums2 = [4,9,5]
print(s.intersection(nums1,nums2))