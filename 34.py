class Solution(object):
    def searchRange(self, nums, target):
        arr = [-1,-1]
        arr2 =[]
        if target not in nums:
            return arr
        if len(nums)==1:
            return [0,0]
        if target == nums[0]:
            return [0,0]
        for i in range(len(nums)):
            if nums[i]==target:
                arr2.append(i)
                arr2.append(i+1)
                break
        return arr2

sol = Solution()
nums = [1,3]
target = 1
print(sol.searchRange(nums,target))
