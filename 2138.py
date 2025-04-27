class Solution(object):
    def divideString(self, s, k, fill):
        out = []
        st = ''
        for i in s:
            if len(st) == k:
                out.append(st)
                st = ''
            st = st + i
        out.append(st)
        if len(out[-1]) != k:
            nl = k - len(out[-1])
            for i in range(nl):
                out[-1] += fill
        return out


s = "abcdefghij"
k = 3
fill = "x"
sol = Solution()
print(sol.divideString(s,k,fill))