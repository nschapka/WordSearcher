import unittest
from inputReader import inputReader
from inputParser import inputParser
from wordFinder  import wordFinder
from letter      import letter

class WordSearchTests(unittest.TestCase):

    # -----------
    # inputReader
    # -----------

    def testInputReaderInit(self):
        testReader = inputReader('C://users/nschapka/desktop/input.txt')
        self.assertEqual(testReader.filePath, 'C://users/nschapka/desktop/input.txt')

    def testInputReaderFindsFile(self):
        try:
            testReader = inputReader('C://users/nschapka/desktop/input.txt')
            fileObject = open(testReader.filePath)
            self.assertTrue(fileObject)
        finally:
            fileObject.close()

    def testInputReaderReadsTextAndInputNotBlank(self):
        try:
            testReader = inputReader('C://users/nschapka/desktop/input.txt')
            fileObject = open(testReader.filePath)
            inputText  = testReader.readText(fileObject)
            self.assertTrue(inputText)  # this test necessitates a file that isn't blank
        finally:
            fileObject.close()

    # -----------
    # inputParser
    # -----------

    def testInputParserGrabsTextFromInputReader(self):
        try:
            testReader = inputReader('C://users/nschapka/desktop/input.txt')
            testParser = inputParser()

            fileObject = open(testReader.filePath)
            inputText = testReader.readText(fileObject)
            testParser.getTextToParse(testReader)

            self.assertTrue(testParser.textToParse)

        finally:
            fileObject.close()

    def testInputParserGetsCorrectTargetWords(self):
        testParser = inputParser()
        testParser.textToParse = ['YES,NO,MAYBE,I,DONT,KNOW']

        targetWords = testParser.parseTargetWords()

        self.assertEqual(targetWords, ['YES', 'NO', 'MAYBE', 'I', 'DONT', 'KNOW'])

    def testInputParserReadsGridIntoArray(self):
        testParser = inputParser()
        testParser.textToParse = ['can you repeat the question?', 'A,B,C', 'D,E,F', 'G,H,I']

        wordSearchGrid = testParser.generateWordSearchGrid()
        gridLetters = [[letter.char for letter in row] for row in wordSearchGrid]
        gridPositions = [[letter.position for letter in row] for row in wordSearchGrid]

        self.assertEqual(gridLetters, [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])
        self.assertEqual(gridPositions, [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]])

    # ------
    # letter
    # ------

    def testLetterInit(self):
        testLetter = letter('a', 1, 0)
        self.assertTrue(testLetter)
        self.assertEqual(testLetter.char, 'a')
        self.assertEqual(testLetter.position, (1, 0))

    # ----------
    # wordFinder
    # ----------

    def testWordFinderInit(self):
        testFinder = wordFinder()
        self.assertTrue(testFinder)

    def testForwardHorizontalGridGeneration(self):
        testFinder = wordFinder()
        testParser = inputParser()
        testParser.textToParse = ['youre not the boss of me now', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = testParser.generateWordSearchGrid()

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        # this test is unnecessary -- the forward grid is just the regular grid -- but imo it would look weird if it were missing.
        self.assertEqual(gridLetters, [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])
        self.assertEqual(gridPositions, [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]])

    def testBackwardHorizontalGridGeneration(self):
        testFinder = wordFinder()
        testParser = inputParser()
        testParser.textToParse = ['youre not the boss of me now', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = testFinder.generateBackwardHorizontal(testParser.generateWordSearchGrid())

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        self.assertEqual(gridLetters, [['C', 'B', 'A'], ['F', 'E', 'D'], ['I', 'H', 'G']])
        self.assertEqual(gridPositions, [[(2, 0), (1, 0), (0, 0)], [(2, 1), (1, 1), (0, 1)], [(2, 2), (1, 2), (0, 2)]])

    def testForwardVerticalGridGeneration(self):
        testFinder = wordFinder()
        testParser = inputParser()
        testParser.textToParse = ['youre not the boss of me now', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = testFinder.generateForwardVertical(testParser.generateWordSearchGrid())

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        self.assertEqual(gridLetters, [['A', 'D', 'G'], ['B', 'E', 'H'], ['C', 'F', 'I']])
        self.assertEqual(gridPositions, [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]])

    def testBackwardVerticalGridGeneration(self):
        testFinder = wordFinder()
        testParser = inputParser()
        testParser.textToParse = ['and youre not so big', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = testFinder.generateBackwardVertical(testParser.generateWordSearchGrid())

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        self.assertEqual(gridLetters, [['G', 'D', 'A'], ['H', 'E', 'B'], ['I', 'F', 'C']])
        self.assertEqual(gridPositions, [[(0, 2), (0, 1), (0, 0)], [(1, 2), (1, 1), (1, 0)], [(2, 2), (2, 1), (2, 0)]])

    def testDownRightDiagonalGridGeneration(self):
        # defining this as top left to bottom right
        testFinder = wordFinder()
        testParser = inputParser()
        testParser.textToParse = ['and youre not so big', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = testFinder.generateForwardRightDiagonal(testParser.generateWordSearchGrid())

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        # ABC          C
        # DEF  becomes BF
        # GHI          AEI
        #              DH
        #              G

        self.assertEqual(gridLetters, [['C'], ['B', 'F'], ['A', 'E', 'I'], ['D', 'H'], ['G']])
        self.assertEqual(gridPositions, [[(2, 0)], [(1, 0), (2, 1)], [(0, 0), (1, 1), (2, 2)], [(0, 1), (1, 2)], [(0, 2)]])

    def testUpRightDiagonalGridGeneration(self):
        # defining this as top left to bottom right
        testFinder = wordFinder()
        testParser = inputParser()
        testParser.textToParse = ['youre not the boss of me now', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = testFinder.generateUpRightDiagonal(testParser.generateWordSearchGrid())

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        # ABC          A
        # DEF  becomes DB
        # GHI          GEC
        #              HF
        #              I

        self.assertEqual(gridLetters, [['A'], ['D', 'B'], ['G', 'E', 'C'], ['H', 'F'], ['I']])
        self.assertEqual(gridPositions, [[(0, 0)], [(0, 1), (1, 0)], [(0, 2), (1, 1), (2, 0)], [(1, 2), (2, 1)], [(2, 2)]])

    def testDownLeftDiagonalGridGeneration(self):
        # defining this as top left to bottom right
        testFinder = wordFinder()
        testParser = inputParser()
        testParser.textToParse = ['youre not the boss of me now', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = testFinder.generateUpRightDiagonal(testParser.generateWordSearchGrid())

        # this is just Up Right backwards, no need for another function.
        testLetters = [row[::-1] for row in testLetters]

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        # ABC          A
        # DEF  becomes BD
        # GHI          CEG
        #              FH
        #              I

        self.assertEqual(gridLetters, [['A'], ['B', 'D'], ['C', 'E', 'G'], ['F', 'H'], ['I']])
        self.assertEqual(gridPositions, [[(0, 0)], [(1, 0), (0, 1)], [(2, 0), (1, 1), (0, 2)], [(2, 1), (1, 2)], [(2, 2)]])

    def testUpLeftDiagonalGridGeneration(self):
        # defining this as top left to bottom right
        testFinder = wordFinder()
        testParser = inputParser()
        testParser.textToParse = ['and youre not so big', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = testFinder.generateForwardRightDiagonal(testParser.generateWordSearchGrid())

        # this one is just the down right flipped horizontally, no need for another function.
        testLetters = [row[::-1] for row in testLetters]

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        # ABC          C
        # DEF  becomes FB
        # GHI          IEA
        #              HD
        #              G

        self.assertEqual(gridLetters, [['C'], ['F', 'B'], ['I', 'E', 'A'], ['H', 'D'], ['G']])
        self.assertEqual(gridPositions, [[(2, 0)], [(2, 1), (1, 0)], [(2, 2), (1, 1), (0, 0)], [(1, 2), (0, 1)], [(0, 2)]])



if __name__ == '__main__':
    unittest.main()
