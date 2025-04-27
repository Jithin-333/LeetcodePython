class Solution(object):
    def findSpecialInteger(self, arr):
        quat = len(arr)//4
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] > quat:
                return i


sol = Solution()
arr = [1,1]
print(sol.findSpecialInteger(arr))