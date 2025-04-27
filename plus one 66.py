class Solution(object):
    def plusOne(self, digits):
        s=""
        for i in digits:
            s = s + str(i)
        s = str(int(s)+1)
        s = list(s)
        arr=[]
        for i in s:
            arr.append(int(i))

        return arr

digits = [9]
sol=Solution()
print(sol.plusOne(digits))