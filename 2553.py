class Solution(object):
    def separateDigits(self, nums):
        out = []
        for i in nums:
            if len(str(i)) > 1:
                for char in str(i):
                    out.append(int(char))
            else:
                out.append(i)
        return out
        
