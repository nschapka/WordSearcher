from letter import letter

class inputParser:

    def __init__(self):
        pass

    def getTextToParse(self, inputReader):
        self.textToParse = inputReader.inputText

    def parseTargetWords(self):
        targetWords = str.split(self.textToParse[0], ',')
        if len(targetWords) == 1 and targetWords[0] == '':
            raise ValueError('no target words found in file')
        return targetWords

    def generateWordSearchGrid(self):
        wordSearchGrid = [str.split(line, ',') for line in (self.textToParse[1:])]
        size = len(self.textToParse) - 1
        if len(wordSearchGrid) != len(wordSearchGrid[-1]):
            raise ValueError('word search grid is not a square')
        for row in wordSearchGrid:
            for gridPosition in row:
                if len(gridPosition) != 1:
                    raise ValueError('word search grid not properly separated with commas')

        return [[letter(wordSearchGrid[y][x], x, y) for x in range(size)] for y in range(size)]
