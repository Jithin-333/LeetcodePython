class Solution(object):
    def countGoodSubstrings(self, s):
        st = []
        temp=""
        for i in range(len(s) - 2):
            j = i
            while len(temp) < 3:
                temp += s[j]
                j = j + 1
            st.append(temp)
            temp = ''
        count = 0
        for i in st:
            if len(i) == len(set(i)):
                count += 1
        return count

s = "aababcabc"
sol = Solution()
print(sol.countGoodSubstrings(s))