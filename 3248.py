class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        position = 0
        for i in commands:
            if i == "DOWN":
                position += n
            elif i == "UP":
                position -= n
            elif i == "RIGHT":
                position += 1
            else:
                position -= 1
        return position
        
