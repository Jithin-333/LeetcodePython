class Solution:
    def findNumbers(self, nums):
        res=0
        for i in nums:
            count = 0
            while i != 0:
                s = i//10
                i = s
                count+=1
            
            if count % 2 == 0:
                res += 1
        return res
    
nums = [555,901,482,1771]
sol = Solution()
print(sol.findNumbers(nums))