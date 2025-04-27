class Solution(object):
    def kthDistinct(self, arr, k):
        dic ={}
        for i in arr:
            if i in dic:
                dic.pop(i)
            else:
                dic[i] = 1
        l = [x for x in dic.keys()]
        if len(l) < k:
            return ""
        return l[k-1]



sol = Solution()
# arr = ["a","b","a"]
# k = 3
# arr = ["aaa","aa","a"]
# k = 1
arr = ["d","b","c","b","c","a"]
k = 2

print(sol.kthDistinct(arr,k))
