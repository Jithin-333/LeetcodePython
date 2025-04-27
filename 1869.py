class Solution:
    def checkZeroOnes(self, s):
        dic = {1:0,0:0}
        count1 = 0
        count0 = 0
        for i in s:
            if i == '1':
                if dic[0] < count0:
                    dic[0] = count0
                count1 += 1
                count0 = 0
            else:
                if dic[1] < count1:
                    dic[1] = count1
                count1 = 0
                count0 += 1

        if dic[1] < count1:
            dic[1] = count1
        if dic[0] < count0:
            dic[0] = count0
        return dic[1] > dic[0]





sol = Solution()
s = "110"
print(sol.checkZeroOnes(s))