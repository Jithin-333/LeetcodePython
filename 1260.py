class Solution(object):
    def shiftGrid(self, grid, k):
        len_row = len(grid[0])
        sing_grid = [x for i in grid for x in i]
        for _ in range(k):
            j =sing_grid.pop(-1)
            temp = []
            temp.append(j)
            sing_grid = temp + sing_grid
        result = []
        res = []
        for i in sing_grid:
            res.append(i)
            if len(res) == len_row:
                result.append(res)
                res = []
        return result

sol = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 9
print(sol.shiftGrid(grid,k))