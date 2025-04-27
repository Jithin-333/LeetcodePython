class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        arr=[]
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    if j+1 != len(nums2):
                        if i < nums2[j+1]:
                            arr.append(nums2[j+1])
                        else:arr.append(-1)
                    else:
                        arr.append(-1)
        return arr
sol=Solution()
nums1=[1,3,5,2,4]
nums2=[6,5,4,3,2,1,7]
print(sol.nextGreaterElement(nums1,nums2))


