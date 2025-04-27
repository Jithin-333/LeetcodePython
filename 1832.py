import string


class Solution(object):
    def checkIfPangram(self, sentence):
        # return sorted(set(sentence)) == list(string.ascii_lowercase)
        return len(set(sentence)) == 26

sol =  Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(sol.checkIfPangram(sentence))