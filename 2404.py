class Solution(object):
    def mostFrequentEven(self, nums):
        evenarr = []
        for i in nums:
            if i % 2 == 0:
                evenarr.append(i)
                
        if len(evenarr) == 0:
            return -1
        
        freq = {}
        for num in evenarr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
       
        most_frequent = -1
        highest_freq = 0
        
        for num, count in freq.items():
            if count > highest_freq or (count == highest_freq and num < most_frequent):
                highest_freq = count
                most_frequent = num
        
        return most_frequent


sol = Solution()
nums = [10000]
print(sol.mostFrequentEven(nums)) 
