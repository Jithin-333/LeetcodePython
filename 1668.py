class Solution(object):
    def maxRepeating(self, sequence, word):
        if word not in sequence:
            return 0

        sequence = sequence.replace(word,'*')
        count = 0
        for i in sequence:
            if i == ' ':
                count += 1
        return sequence


sol = Solution()
# sequence = "ababc"
# word = "ab"
sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"
print(sol.maxRepeating(sequence,word))

