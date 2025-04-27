class Solution(object):
    def stringMatching(self, words):
        arr=[]
        for i in words:
            for j in words:
                if j in i and j != i:
                    arr.append(j)

        return list(set(arr))
sol = Solution()
words = ["leetcoder","leetcode","od","hamlet","am"]
print(sol.stringMatching(words))