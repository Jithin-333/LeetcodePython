class Solution(object):
    def decrypt(self, code, k):
        out = []
        for i in range(len(code)):
            sum = 0
            if k < 0:
                for j in range(1,abs(k+1)):
                    sum += code[i-j]
                out.append(sum)
            elif k > 0:
                for j in range(1,k+1):
                    sum += code[i+j]
                out.append(sum)
        return out



code = [2,4,9,3]
k = -2
sol = Solution()
print(sol.decrypt(code,k))