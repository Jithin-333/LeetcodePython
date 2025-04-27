class Solution(object):
    def fizzBuzz(self, n):
        i = 1
        arr=[]
        for i in range(n):
            ele = i+1
            if ele % 3 == 0 and ele % 5 == 0:
                arr.append('FizzBuzz')
            elif ele % 3 == 0:
                arr.append('Fizz')
            elif ele % 5 == 0:
                arr.append('Buzz')
            else:
                arr.append(str(ele))
        return arr

s = Solution()
n = 15
print(s.fizzBuzz(n))