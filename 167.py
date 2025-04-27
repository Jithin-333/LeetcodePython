class Solution(object):
    def twoSum(self, numbers, target):
        start = 0
        end = len(numbers)-1
        while start < end :
            sum = numbers[start]+numbers[end]
            if sum == target:
                return [start+1,end+1]
            elif sum < target:
                start = start + 1
            else:
                end = end - 1

sol = Solution()
numbers =[2,7,11,15]
target = 7
print(sol.twoSum(numbers,target))
