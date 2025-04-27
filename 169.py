class Solution(object):
    def majorityElement(self, nums):
        fre = {}
        n = len(nums) // 2
        for i in nums:
            if i in fre:
                fre[i] += 1
            else:
                fre[i] = 1

        for i in fre:
            if fre[i] > n:
                return i
        

nums = [2,2,1,1,1,2,2]
sol = Solution()
print(sol.majorityElement(nums))