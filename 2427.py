# class Solution(object):
#     def commonFactors(self, a, b):
#         res = []
#         def recfact(fact):
#             if fact == 0:
#                 return
#             if a % fact == 0 and b % fact == 0:
#                 res.append(fact)
#             recfact(fact - 1)
#
#         recfact(min(a, b))
#         return res
#
# sol = Solution()
# a = 12
# b = 6
# print(sol.commonFactors(a,b))

import copy

arr = []


size = int(input("Enter the number of elements in the array: "))


for i in range(size):
   value = int(input("Enter element {}: ".format(i + 1)))
   arr.append(value)


print("The entered array is:", arr)


arr2 = arr.copy()
print("copy of first array: ", arr2)


size_add = int(input("Enter the number of extra elements to be added: "))


for i in range(size_add):


   value = int(input("Enter element the element to add: "))
   arr2.append(value)


print("Added array is: ", arr2)
