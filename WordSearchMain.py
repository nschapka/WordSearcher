from letter import letter
from inputReader import inputReader
from inputParser import inputParser
from gridReorienter import gridReorienter
from wordFinder import wordFinder

def wordSearchMain():
    reader = inputReader('C://users/nschapka/desktop/input2.txt')
    inputFile = open(reader.filePath)
    parser = inputParser()
    reorienter = gridReorienter()
    finder = wordFinder()
    searchGrids = []
    foundWords = []

    # parse the input text and generate the first grid
    parser.textToParse = reader.readText(inputFile)
    targetWords = parser.parseTargetWords()
    baseGrid = parser.generateWordSearchGrid()
    searchGrids.append(baseGrid)

    # add the rest of the reoriented grids
    searchGrids.append(reorienter.generateBackwardHorizontal(baseGrid))
    searchGrids.append(reorienter.generateForwardVertical(baseGrid))
    searchGrids.append(reorienter.generateBackwardVertical(baseGrid))
    searchGrids.append(reorienter.generateForwardRightDiagonal(baseGrid))
    searchGrids.append(reorienter.generateUpRightDiagonal(baseGrid))
    searchGrids.append([row[::-1] for row in reorienter.generateForwardRightDiagonal(baseGrid)])  # up left diagonal
    searchGrids.append([row[::-1] for row in reorienter.generateUpRightDiagonal(baseGrid)])  # down left diagonal

    # search for words
    for target in targetWords:
        for grid in searchGrids:
            foundWord = finder.findWords(grid, target)
            if foundWord:
                foundWords.append(foundWord)
                foundWord = None
                break

    for word in foundWords:
        print(word)

if __name__ == '__main__':
    wordSearchMain()