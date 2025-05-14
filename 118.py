class Solution(object):
    def generate(self, numRows):
        rowOut = []
        i = 1
        def generateArr(rowOut,numRows, i):
            if i == numRows + 1:
                return rowOut
            if i == 1:
                rowOut.append([1])
                i += 1
                return generateArr(rowOut, numRows, i)
            if i == 2:
                rowOut.append([1,1])
                i += 1
                return generateArr(rowOut, numRows, i)
            arr = [1]
            prevArr = rowOut[-1]
            for j in range(len(prevArr) - 1):
                s = prevArr[j] + prevArr[j + 1]
                arr.append(s)
            arr.append(1)
            rowOut.append(arr)
            i += 1
            return generateArr(rowOut, numRows, i)
        return generateArr(rowOut,numRows, i)
