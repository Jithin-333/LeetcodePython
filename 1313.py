class Solution(object):
    def decompressRLElist(self, nums):
        num1 = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        num2 = [nums[i] for i in range(len(nums)) if i % 2 != 0]
        res =[]
        for i in num1:
            for _ in range(i):
                res.append(num2[0])
            num2.pop(0)
        return res


nums = [1,2,3,4]
sol = Solution()
print(sol.decompressRLElist(nums))