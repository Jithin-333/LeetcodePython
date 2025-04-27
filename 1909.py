# class Solution(object):
#     def canBeIncreasing(self, nums):
#         for i in nums:
#             sortnum=sorted(nums)
#             x=nums
#             x.remove(i)
#             sortnum.remove(i)
#             print(sortnum)
#             if len(x) == 1:
#                 return True
#             if x == sortnum:
#                 return True
#         return False
import copy
class Solution(object):
    def canBeIncreasing(self, nums):
        for i in range(len(nums)):
            x = copy.copy(nums)
            x.remove(nums[i])
            c=0
            for j in range(len(x)-1):
                if x[j] < x[j+1]:
                    c += 1
            if c == len(x)-1:
                return True
        return False


sol=Solution()
nums = [42,50,54,74,84,86,88,93,104,127,143,160,164,169,170,181,209,223,225,231,247,257,262,274,282,306,307,320,346,357,378,381,387,392,394,404,423,437,444,456,476,491,507,524,527,528,537,558,566,574,169,584,585,609,621,626,632,644,653,661,662,670,676,698,704,710,718,719,730,735,737,746,748,755,776,782,785,795,802,812,822,828,863,866,870,872,877,899,905,909,919,929,940,944,961,963,980,981]
print(sol.canBeIncreasing(nums))