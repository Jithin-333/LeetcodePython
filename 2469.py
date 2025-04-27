class Solution(object):
    def convertTemperature(self, celsius):
        return [celsius + 273.15] + [celsius * 1.80 + 32.00]

sol = Solution()
celsius = 36.50
print(sol.convertTemperature(celsius))

