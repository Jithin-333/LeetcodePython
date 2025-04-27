import string
class Solution(object):

    def numberOfSpecialChars(self, word):
        word = set(word)
        cap = list(string.ascii_uppercase)
        small = list(string.ascii_lowercase)
        count = 0
        for i in word:
            if i in cap:
                if (i.lower()) in word:
                    count += 1
        return count

word = "abc"
sol = Solution()
print(sol.numberOfSpecialChars(word))




