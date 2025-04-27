class Solution(object):
    def capitalizeTitle(self, title):
        ls = title.split()
        out=[]
        for i in ls:
            if len(i) <= 2:
                out.append(i.lower())
            else:
                out.append(i.lower().capitalize())
        return ' '.join(out)



title = "capiTalIze to tHe titLe"
sol = Solution()
print(sol.capitalizeTitle(title))