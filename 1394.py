class Solution(object):
    def findLucky(self, arr):
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        lucky_num = []
        for i in dic:
            if dic[i] == i:
                lucky_num.append(i)
        if lucky_num:
            return max(lucky_num)
        return -1
