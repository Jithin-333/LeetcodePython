class Solution(object):
    def minExtraChar(self, s, dictionary):
        new = ''
        dictionary = set(dictionary)
        print(dictionary)
        for i in s:
            new += i
            if new in dictionary:
                s = s.replace(new,'')

        return len(s)



s = "leetscode"
dictionary = ["leet","code","leetcode"]
sol = Solution()
print(sol.minExtraChar(s,dictionary))

