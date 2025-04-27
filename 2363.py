class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        # dic={}
        # new_list = [x for x in items1 + items2]
        # for i in new_list:
        #     if i[0] in dic:
        #         dic[i[0]] += i[1]
        #     else:
        #         dic[i[0]] = i[1]
        # res = [[x,dic[x]] for x in dic]
        # return res
        dic  ={}
        for item,weight in items1 + items2:
            if item in dic:
                dic[item] += weight
            else:
                dic[item] = weight
        return sorted([[x,dic[x]] for x in dic])



items1 = [[1,1]]
items2 = [[1000,1000]]
sol = Solution()
print(sol.mergeSimilarItems(items1,items2))