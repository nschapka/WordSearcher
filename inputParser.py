from letter import letter

class inputParser:

    def __init__(self):
        pass

    def getTextToParse(self, inputReader):
        self.textToParse = inputReader.inputText

    def parseTargetWords(self):
        targetWords = str.split(self.textToParse[0], ',')
        return targetWords

    def generateWordSearchGrid(self):
        wordSearchGrid = [str.split(line, ',') for line in (self.textToParse[1:])]
        size = len(self.textToParse) - 1
        return [[letter(wordSearchGrid[x][y], x, y) for y in range(size)] for x in range(size)]
