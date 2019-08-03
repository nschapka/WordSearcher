class gridReorienter:
    def __init__(self):
        pass

    def __generateDiagPyramid(self, size, backward):
        # generates a jagged array of coordinates based on the input size. given eg. 3
        # 2                       0
        # 1 2                     1 0
        # 0 1 2  and if backward: 2 1 0
        # 0 1                     2 1
        # 0                       2
        # these are used to address coordinates of letters in a grid to generate diagonal strings to search
        if not backward:
            coordArr = range(size)
        else:
            coordArr = range(size)[::-1]

        coords = []

        for x in range(size)[::-1]:
            coords.append(coordArr[x:])
        for x in range(1, size)[::-1]:
            coords.append(coordArr[:x])

        return coords

    def generateForwardHorizontal(self, testGrid):
        return ["".join(row) for row in testGrid]

    def generateBackwardHorizontal(self, testGrid):
        return [row[::-1] for row in testGrid]

    def generateForwardVertical(self, testGrid):
        # defining forward as top to bottom here
        return [[testGrid[row][col] for row in range(len(testGrid[0]))] for col in range(len(testGrid))]

    def generateBackwardVertical(self, testGrid):
        # bottom to top
        verticalGrid = [[testGrid[row][col] for row in range(len(testGrid[0]))] for col in range(len(testGrid))]
        return [row[::-1] for row in verticalGrid]

    def generateForwardRightDiagonal(self, testGrid):
        # forward right diagonal = top left to bottom right
        xCoords = self.__generateDiagPyramid(len(testGrid), False)
        yCoords = xCoords[::-1]

        coords = [list(zip(xCoords[n], yCoords[n])) for n in range(len(xCoords))]

        outputGrid = [[testGrid[num[1]][num[0]] for num in n] for n in coords]

        return outputGrid

    def generateUpRightDiagonal(self, testGrid):
        yCoords = self.__generateDiagPyramid(len(testGrid), True)
        xCoords = [row[::-1] for row in yCoords]

        coords = [list(zip(xCoords[n], yCoords[n])) for n in range(len(xCoords))]

        outputGrid = [[testGrid[num[1]][num[0]] for num in n] for n in coords]

        return outputGrid

