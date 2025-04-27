def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        for s in strs:b

            if i == len(s) or s[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))

