class Solution(object):
    def halvesAreAlike(self, s):
        l = len(s)
        h = l//2
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        first_half = s[:h]
        second_half = s[h:]
        dic_first = {'vowel':0}
        dic_second = {'vowel':0}
        for i in first_half:
            if i in vowel:
                dic_first['vowel'] += 1
            else:
                pass
        for i in second_half:
            if i in vowel:
                dic_second['vowel'] += 1
            else:
                pass
        return dic_second == dic_first





s = "book"
sol = Solution()
print(sol.halvesAreAlike(s))