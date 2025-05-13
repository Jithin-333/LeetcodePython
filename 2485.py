class Solution(object):
    def pivotInteger(self, n):
        if n == 1:
            return 1
        for i in range(1, n + 1):
            if sum([x for x in range(1,i + 1)]) == sum([j for j in range(i, n + 1)]):
                return i
        else:
            return -1
        
