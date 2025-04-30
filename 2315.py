class Solution(object):
    def countAsterisks(self, s):
        count = 0
        if '|' not in s:
            for i in s:
                if i == '*':
                    count += 1
            return count

        char_list = s.split("|")
        num = 0
        for i in range(len(char_list)):
            if i % 2 == 0:
                for char in range(len(char_list[i])):
                    if char_list[i][char] == "*":
                        count += 1
        return count
