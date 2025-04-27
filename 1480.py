class Solution(object):
    def runningSum(self, nums):
        arr=[]
        s=0
        for i in nums:
            s = s+i
            arr.append(s)
        return arr


sol=Solution()
nums = [1,2,3,4]
print(sol.runningSum(nums))