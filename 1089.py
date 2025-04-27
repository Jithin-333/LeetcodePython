class Solution(object):
    def duplicateZeros(self, arr):
        if 0 not in arr:
            return arr
        l = len(arr)
        arr2=[]
        for i in range(l):
            if len(arr) <= l:
                if arr[i] == 0:
                    arr2.append(arr[i])
                    arr2.append(arr[i])
                else:
                    arr2.append(arr[i])
        for i in range(l):
            arr[i] = arr2[i]

sol = Solution()
nums = [1, 0, 2, 3, 0, 4, 5, 0]
print(sol.duplicateZeros(nums))
