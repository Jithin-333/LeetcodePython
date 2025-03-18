class Solution(object):
    def findPeaks(self, mountain):
        out = []
        for i in range(1,len(mountain)-1):
            if mountain[i-1] < mountain[i] > mountain[i+1]:
                out.append(i)
        return out
