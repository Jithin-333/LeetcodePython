class Solution(object):
    def minOperations(self, s):
        count = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                pass
            else:
                if s[i] == '0':
                    s = s[:i] + '1' + s[-i:]
                else:
                    s = s[:i] + '0' + s[-i:]
                count += 1
        return count


sol = Solution()
s = "1010000"
print(sol.minOperations(s))

count1 = 0
count2 = 0

# for i in range(len(s)):
#     if i % 2 == 0:
#         if s[i] != '0':
#             count1 += 1
#         if s[i] != '1':
#             count2 += 1
#     else:
#         if s[i] != '1':
#             count1 += 1
#         if s[i] != '0':
#             count2 += 1
#
# return min(count1, count2)  correct output
