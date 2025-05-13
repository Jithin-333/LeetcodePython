class Solution(object):
    def alternateDigitSum(self, n):
        digit_sum = 0
        while n > 0:
            if len(str(n)) % 2 != 0:
                digit_sum += (n % 10)
                n = n // 10
            else:
                digit_sum = digit_sum + (-(n % 10))
                n = n // 10
        return digit_sum
