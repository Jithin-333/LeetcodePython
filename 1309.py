class Solution(object):
    def freqAlphabets(self, s):
        key = [x for x in range(1,27)]
        val = [x for x in string.ascii_lowercase]
        dic = {key: val for (key,val) in zip(key,val) }

        str_char = ""
        i = len(s)-1
        while i >= 0:
            if s[i] == "#":
                num = s[i-2]
                num += s[i-1]
                str_char += dic[int(num)]
                i = i - 3
            else:
                str_char += dic[int(s[i])]
                i = i - 1
        return str_char[::-1]
