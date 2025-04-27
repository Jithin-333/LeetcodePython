class Solution(object):
    def minimumSum(self, num):
        new_num=[]
        for i in str(num):
            new_num.append(i)
        res = []
        for _ in range(4):
            if new_num == []:
                break
            j = min(new_num)
            new_num.remove(j)
            i = max(new_num)
            new_num.remove(i)
            res.append(j+i)
        return int(res[0]) + int(res[1])

num = 4019
sol = Solution()
print(sol.minimumSum(num))