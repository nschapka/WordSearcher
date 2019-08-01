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
