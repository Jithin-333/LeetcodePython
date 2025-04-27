class Solution(object):
    def uniqueOccurrences(self, arr):
        cnt = []
        check = []
        for i in range(len(arr)):
            count = 1
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    count += 1
            if arr[i] not in check:
                cnt.append(count)
            check.append(arr[i])
            if len(cnt) == len(set(arr)):
                break
        return len(cnt) == len(set(cnt))

sol = Solution()
arr = [-3,0,1,-3,1,1,1,-3,10,0]
x = sol.uniqueOccurrences(arr)
print(x)
# from collections import Counter
# arr = [-3,0,1,-3,1,1,1,-3,10,0]
# counts=Counter(arr).values()
# print(counts)
# if len(counts)==len(set(counts)):
#     print(True)
# else:
#     print(False)