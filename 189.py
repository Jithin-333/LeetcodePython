class Solution(object):
    def rotate(self, nums, k):
        arr=[]
        i=1
        while i <= k:
            arr.append(nums[-1])
            nums.pop(-1)
            i += 1
        arr.reverse()
        return arr + nums

sol = Solution()
nums=[-1,-100,3,99]
k = 2
print(sol.rotate(nums,k))