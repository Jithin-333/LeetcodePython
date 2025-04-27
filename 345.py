class Solution(object):
    def reverseVowels(self, s):
        vow = ['a','e','i','o','u','A','E','I','O','U']
        st = ""
        rev=""
        for i in s:
            if i in vow:
                st = st + i
        st = list(st[::-1])
        for i in s:
            if i in vow:
                rev = rev + st[0]
                st.remove(st[0])
            else:
                rev = rev + i
        return rev
s = "leetcode"
sol = Solution()
print(sol.reverseVowels(s))