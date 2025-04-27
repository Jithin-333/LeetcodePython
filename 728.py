class Solution(object):
    def selfDividingNumbers(self, left, right):
        li = []
        for i in range(left, right + 1):
            if "0" not in str(i):
                for char in str(i):
                    if i % int(char) == 0:
                        pass
                    else:
                        break
                else:
                    li.append(i)
        return li
