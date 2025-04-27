class Solution(object):
    def countWords(self, words1, words2):
        dic = {}
        for i in words1:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        dic1 = {}
        for i in words2:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        count = 0
        for i in words1:
            if i in words2:
                if dic[i] == 1 and dic1[i] == 1:
                    count += 1
        return count



sol = Solution()
words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
print(sol.countWords(words1, words2))