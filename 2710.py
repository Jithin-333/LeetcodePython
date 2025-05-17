class Solution(object):
    def removeTrailingZeros(self, num):
        while num[-1] == '0':
            num = num[:len(num)-1]
        return num
