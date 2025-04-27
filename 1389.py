class Solution(object):
    # def createTargetArray(self, nums, index):
    #     target = [None for _ in range(len(nums))]
    #     l = len(nums)
    #     for i in range(len(nums)):
    #         if target[index[i]] == None:
    #             target[index[i]] = nums[i]
    #         else:
    #             j = l-1
    #             while (index[i] < j):
    #                 target[j],target[j-1] = target[j-1],target[j]
    #                 j = j - 1
    #             target[index[i]] = nums[i]
    #     return target
    def createTargetArray(self, nums, index):
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target


sol = Solution()
nums = [0,1,2,3,4]
index = [0,1,2,2,1]


print(sol.createTargetArray(nums,index))