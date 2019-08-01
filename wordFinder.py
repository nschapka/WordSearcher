class wordFinder:
    def __init__(self):
        pass

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
        size = len(testGrid)  # should be square
        xCoordArr = range(size)
        xCoords = []
        yCoordArr = range(size)
        yCoords = []
        coords = []

        for x in range(size)[::-1]:
            xCoords.append(xCoordArr[x:])
        for x in range(1, size)[::-1]:
            xCoords.append(xCoordArr[:x])

        yCoords = xCoords[::-1]

        coords = [list(zip(xCoords[n], yCoords[n])) for n in range(len(xCoords))]

        outputGrid = [[testGrid[num[1]][num[0]] for num in n] for n in coords]

        return outputGrid

