class Solution(object):
    def frequencySort(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        sorted_list = sorted(nums, key=lambda x: (dic[x], -x))

        return sorted_list

sol = Solution()
nums = [1,1,2,2,2,3]
print(sol.frequencySort(nums))

