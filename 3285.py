class Solution(object):
    def stableMountains(self, height, threshold):
        res = []
        for i in range(1 , len(height)):
            if height[i-1] > threshold:
                res.append(i)
        return res




sol = Solution()
height = [1,2,3,4,5]
threshold = 2
print(sol.stableMountains(height,threshold))