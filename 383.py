class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for i in magazine:
            if i in ransomNote:
                ransomNote = ransomNote.replace(i,'',1)
        return ransomNote == ''


sol = Solution()
ransomNote = "aa"
magazine = "ab"
print(sol.canConstruct(ransomNote,magazine))