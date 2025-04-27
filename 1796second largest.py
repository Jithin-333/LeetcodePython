class Solution(object):
    def secondHighest(self, s):
        num = [int(x) for x in s if x.isdigit()]
        num = sorted(list(set(num)),reverse=True)
        if len(num) < 2:
            return -1
        return num[1]

sol = Solution()
secondlargest = sol.secondHighest("dfa1234dk56dk21afd")
print(secondlargest)