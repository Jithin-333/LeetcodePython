
class Solution(object):
    def flipAndInvertImage(self, image):
        sz = len(image[0])
        for i in image:
            i.reverse()
            for j in range(sz):
                if i[j] == 0:
                    i[j] = 1
                else:
                    i[j] = 0
        return image




sol = Solution()
image = [[1,1,0],[1,0,1],[0,0,0]]
print(sol.flipAndInvertImage(image))