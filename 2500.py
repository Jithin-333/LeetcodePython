class Solution(object):
    def deleteGreatestValue(self, grid):
        k = len(grid[0])
        new_list = []
        for i in range(k):
            li1 = []
            for li in grid:
                s = max(li)
                li.remove(s)
                li1.append(s)
            new_list.append(max(li1))
        return sum(new_list)
