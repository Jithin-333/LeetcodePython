class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        new=[]
        arr1.sort()
        for i in arr2:
            s = arr1.count(i)
            for j in range(s):
                new.append(i)
        for i in arr1:
            if i not in arr2:
                new.append(i)
        return new


sol = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(sol.relativeSortArray(arr1,arr2))
