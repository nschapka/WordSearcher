class wordFinder:
    def __init__(self):
        pass

    def generateForwardHorizontal(self, testGrid):
        return ["".join(row) for row in testGrid]

    def generateBackwardHorizontal(self, testGrid):
        backwardGrid = [row[::-1] for row in testGrid]
        return ["".join(row) for row in backwardGrid]