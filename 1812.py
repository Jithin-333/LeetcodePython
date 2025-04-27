class Solution(object):
    def squareIsWhite(self, coordinates):
        ev = "a,c,e,g"
        if coordinates[0] in ev:
            return int(coordinates[1]) % 2 == 0
        return int(coordinates[1]) % 2 != 0

coordinates = "f4"
sol = Solution()
print(sol.squareIsWhite(coordinates))