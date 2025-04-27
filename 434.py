class Solution(object):
    def countSegments(self, s):
        s = s.split()
        return len(s)
        # ls = ""
        # sls = []
        # for i in s:
        #     if i == " ":
        #         sls.append(ls)
        #         ls = ""
        #     else:
        #         ls = ls + i
        # sls.append(ls)
        # print(sls)
        # count = 0
        # for _ in range(len(sls)):
        #     count += 1
        # return count


s = "Hello, my name is John"
sol = Solution()
print(sol.countSegments(s))
