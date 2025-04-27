from datetime import datetime
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        return abs((d2 - d1).days)



date1 = "2020-01-15"
date2 = "2019-12-31"
sol = Solution()
print(sol.daysBetweenDates(date1,date2))