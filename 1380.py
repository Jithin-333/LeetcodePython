class Solution(object):
    def luckyNumbers(self, matrix):
        sz = len(matrix[0])
        out = []
        for i in range(sz):
            test = []
            for u in matrix:
                test.append(u[i])
            out.append(test)
        new_arr=[]
        for i in matrix:
            new_arr.append(min(i))
        sec_arr = []
        for j in out:
            sec_arr.append(max(j))
        res = []
        for i in new_arr:
            if i in sec_arr:
                res.append(i)
        return res



sol = Solution()
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(sol.luckyNumbers(matrix))