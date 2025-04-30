class Solution(object):
    def numberOfPairs(self, nums):
        count = 0
        bal = 0
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] % 2 == 0:
                count += dic[i] // 2
            else:
                count += dic[i] // 2
                bal += dic[i] % 2
        return [count, bal]
