class Solution(object):
    def maxFreqSum(self, s):
        dic = {}
        for i in s:
            if i in dic:
                 dic[i] += 1
            else:
                dic[i] = 1
        vowels = ['a','e','i','o','u']
        vowel_max = 0
        constant_max = 0
        for i in dic:
            if i in vowels:
                if vowel_max < dic[i]:
                    vowel_max = dic[i]
            else:
                if constant_max < dic[i]:
                    constant_max = dic[i]
        return vowel_max + constant_max


sol = Solution()
s = "successes"
print(sol.maxFreqSum(s))
