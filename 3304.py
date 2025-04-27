
class Solution(object):
    def kthCharacter(self, k):
        word = 'a'
        next = lambda char: chr(ord(char) + 1)
        for _ in range((k//2) + 1):
            for i in word:
                word = word + next(i)
                if len(word) == k:
                    return word[k-1]
        return word[0]


sol = Solution()
k = 1
print(sol.kthCharacter(k))

