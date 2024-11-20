class Solution(object):
    def countDigits(self, num):
        numstr = str(num)
        l = [int(x) for x in numstr]
        sum = 0
        for i in l:
            if num % i == 0:
                sum += 1
        return sum
