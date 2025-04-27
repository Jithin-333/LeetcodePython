class Solution(object):
    def mergeTwoLists(self, list1, list2):
        arr = []
        for i in range(50):
            arr.append(list1[i])
            arr.append(list2[i])
            if len(list1) == i+1:
                break

        return arr


sol = Solution()
list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(sol.mergeTwoLists(list1, list2))