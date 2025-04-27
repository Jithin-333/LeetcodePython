class Solution(object):
    def backspaceCompare(self, s, t):
        def backspaceremove(st):
            res = []
            for i in st:
                if i == '#':
                    res.pop(-1)
                else:
                    res.append(i)
            return ''.join(res)
        s = backspaceremove(s)
        t = backspaceremove(t)
        return s == t



sol = Solution()
s = "ab##"
t = "c#d#"
print(sol.backspaceCompare(s,t))



