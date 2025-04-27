class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count = 0
        for i in hours:
            if i >= target:
                count+=1
        return count
sol = Solution()
hours = [0,1,2,3,4]
target = 2
print(sol.numberOfEmployeesWhoMetTarget(hours,target))