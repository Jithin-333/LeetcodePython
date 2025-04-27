class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()
        if len(pattern) != len(s):
            return False

        pat_to_word = {}
        word_to_pat = {}

        for p, word in zip(pattern, s):
            if p in pat_to_word:
                if pat_to_word[p] != word:
                    return False
            if word in word_to_pat:
                if word_to_pat[word] != p:
                    return False

            pat_to_word[p] = word
            word_to_pat[word] = p

        return True


sol = Solution()
pattern = "aaab"
s = "cat cat cat dog"
print(sol.wordPattern(pattern,s))