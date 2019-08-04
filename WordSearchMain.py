from letter import letter
from inputReader import inputReader
from inputParser import inputParser
from gridReorienter import gridReorienter
from wordFinder import wordFinder

def wordSearchMain():
    reader = inputReader('C://users/nschapka/desktop/input.txt')
    inputFile = open(reader.filePath)
    parser = inputParser()
    reorienter = gridReorienter()
    finder = wordFinder()
    searchGrids = []

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
    searchGrids.append(reorienter.generateForwardRightDiagonal(baseGrid)[::-1])  # up left diagonal
    searchGrids.append(reorienter.generateUpRightDiagonal(baseGrid)[::-1])  # down left diagonal





if __name__ == '__main__':
    wordSearchMain()