import string
class Solution(object):
    def reverseDegree(self, s):
        char = string.ascii_lowercase
        li = [x for x in reversed(char)]
        dic = {li[i]:i+1 for i in range(len(li))}

        count = 1
        sum = 0
        for char in s:
            sum += dic[char] * count
            count += 1
        return sum

s = "abc"
sol = Solution()
print(sol.reverseDegree(s))
