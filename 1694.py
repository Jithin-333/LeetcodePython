class Solution(object):
    def reformatNumber(self, number):
        spec = [' ','/','-']
        num = [x for x in number if x not in spec]
        print(num)
        out = ''
        st = ''
        for i in range(len(num)):
            if len(st) == 3:
                out = out + st + '-'
                st = ''
            else:
                st += num[i]
            if i == len(num)-1:
                out += st

        return out





sol = Solution()
number = "1-23-45 6"
print(sol.reformatNumber(number))