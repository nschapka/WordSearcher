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
        return [[letter(wordSearchGrid[y][x], x, y) for x in range(size)] for y in range(size)]
