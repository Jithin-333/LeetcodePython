class Solution(object):
    def checkValid(self, matrix):
        l = len(matrix[0])
        matrix2 = []
        for j in range(l):
            res = []
            for i in matrix:
                res.append(i[j])
            matrix2.append(res)
        for i in matrix:
            if l != len(set(i)):
                return False
        for i in matrix2:
            if l != len(set(i)):
                return False
        return True




matrix = [[1,1,1],[1,2,3],[1,2,3]]
sol = Solution()
print(sol.checkValid(matrix))