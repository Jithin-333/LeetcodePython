class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0
        for item in words:
            item = list(set(item))
            len_item = len(item)
            res = 0
            for char in item:
                if char in allowed:
                    res += 1
            if res == len_item:
                count += 1
        return count


sol = Solution()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(sol.countConsistentStrings(allowed,words))