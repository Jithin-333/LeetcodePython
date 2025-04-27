class Solution(object):
    def divideArray(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] % 2 == 0:
                pass
            else:
                return False
        return True



nums = [3, 2, 3, 2, 2, 2, 2]
sol = Solution()
print(sol.divideArray(nums))