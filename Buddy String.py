class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        res = 0
        if (rec1[0] < rec2[0] and rec2[0] < rec1[2]) or (rec1[0] < rec2[2] and rec2[2] < rec1[2]):
            res = 3
        if (rec1[1] <= rec2[1] and rec2[1] < rec1[3]) or (rec1[1] < rec2[3] and rec2[3] < rec1[3]):
            res = 1
        return res



# rec1 = [0,0,1,1]
# rec2 = [2,2,3,3]

rec1 =[7,8,13,15]
rec2 =[10,8,12,20]



sol = Solution()
print(sol.isRectangleOverlap(rec1, rec2))
