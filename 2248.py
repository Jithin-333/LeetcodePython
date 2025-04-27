class Solution(object):
    def intersection(self, nums):
        arr=[]
        arr2=[]
        for i in range(len(nums)):
            for j in nums[i]:
                arr.append(j)
        arr = list(set(arr))

        for k in range(len(arr)):
            count = 0
            for i in range(len(nums)):
                if arr[k] in nums[i]:
                    count += 1
            if count == len(nums):
                    arr2.append(arr[k])
        return sorted(arr2)



sol = Solution()
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(sol.intersection(nums))
