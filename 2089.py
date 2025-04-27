class Solution(object):
    def targetIndices(self, nums, target):
        nums= sorted(nums)
        arr=[]
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
        return arr

sol = Solution()
nums = [1,2,5,2,3]
target = 2
print(sol.targetIndices(nums,target))