import unittest
import sys
from inputReader     import inputReader
from inputParser     import inputParser
from gridReorienter  import gridReorienter
from letter          import letter
from wordFinder      import wordFinder

class WordSearchTests(unittest.TestCase):

    testFile = ''

    def setUp(self):
        self.testReader = inputReader(self.testFile)
        self.fileObject = open(self.testReader.filePath)
        self.testParser = inputParser()
        self.testReorienter = gridReorienter()
        self.testFinder = wordFinder()

    def tearDown(self):
        self.fileObject.close()

    # -----------
    # inputReader
    # -----------

    def testInputReaderInit(self):
        self.assertEqual(self.testReader.filePath, self.testFile)

    def testInputReaderFindsFile(self):
        try:
            self.assertTrue(self.fileObject)
        finally:
            self.fileObject.close()

    def testInputReaderReadsTextAndInputNotBlank(self):
        try:
            inputText = self.testReader.readText(self.fileObject)
            self.assertTrue(inputText)  # this test necessitates a file that isn't blank
        finally:
            self.fileObject.close()

    # -----------
    # inputParser
    # -----------

    def testInputParserGrabsTextFromInputReader(self):
        try:
            inputText = self.testReader.readText(self.fileObject)
            self.testParser.getTextToParse(self.testReader)

            self.assertTrue(self.testParser.textToParse)

        finally:
            self.fileObject.close()

    def testInputParserGetsCorrectTargetWords(self):
        self.testParser.textToParse = ['YES,NO,MAYBE,I,DONT,KNOW']

        targetWords = self.testParser.parseTargetWords()

        self.assertEqual(targetWords, ['YES', 'NO', 'MAYBE', 'I', 'DONT', 'KNOW'])

    def testInputParserReadsGridIntoArray(self):
        self.testParser.textToParse = ['can you repeat the question?', 'A,B,C', 'D,E,F', 'G,H,I']

        wordSearchGrid = self.testParser.generateWordSearchGrid()
        gridLetters = [[letter.char for letter in row] for row in wordSearchGrid]
        gridPositions = [[letter.position for letter in row] for row in wordSearchGrid]

        self.assertEqual(gridLetters, [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])
        self.assertEqual(gridPositions, [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]])

    def testInputParserFaultsOnNoTargetWords(self):
        self.testParser.textToParse = ['', 'A,B', 'C,D']

        with self.assertRaises(ValueError):
            self.testParser.parseTargetWords()

    def testInputParserFaultsOnRectangularGrid(self):
        self.testParser.textToParse = ['test', 'A,B', 'C,D', 'E,F']

        with self.assertRaises(ValueError):
            self.testParser.generateWordSearchGrid()

    def testInputParserFaultsOnMultiLetterGridSpace(self):
        self.testParser.textToParse = ['test', 'AB,C', 'D,E', 'F,G']

        with self.assertRaises(ValueError):
            self.testParser.generateWordSearchGrid()

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
        self.assertTrue(self.testReorienter)

    def testForwardHorizontalGridGeneration(self):
        self.testParser.textToParse = ['youre not the boss of me now', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = self.testParser.generateWordSearchGrid()

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        self.assertEqual(gridLetters, [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])
        self.assertEqual(gridPositions, [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]])

    def testBackwardHorizontalGridGeneration(self):
        self.testParser.textToParse = ['youre not the boss of me now', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = self.testReorienter.generateBackwardHorizontal(self.testParser.generateWordSearchGrid())

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        self.assertEqual(gridLetters, [['C', 'B', 'A'], ['F', 'E', 'D'], ['I', 'H', 'G']])
        self.assertEqual(gridPositions, [[(2, 0), (1, 0), (0, 0)], [(2, 1), (1, 1), (0, 1)], [(2, 2), (1, 2), (0, 2)]])

    def testForwardVerticalGridGeneration(self):
        self.testParser.textToParse = ['youre not the boss of me now', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = self.testReorienter.generateForwardVertical(self.testParser.generateWordSearchGrid())

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        self.assertEqual(gridLetters, [['A', 'D', 'G'], ['B', 'E', 'H'], ['C', 'F', 'I']])
        self.assertEqual(gridPositions, [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]])

    def testBackwardVerticalGridGeneration(self):
        self.testParser.textToParse = ['and youre not so big', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = self.testReorienter.generateBackwardVertical(self.testParser.generateWordSearchGrid())

        gridLetters = [[letter.char for letter in row] for row in testLetters]
        gridPositions = [[letter.position for letter in row] for row in testLetters]

        self.assertEqual(gridLetters, [['G', 'D', 'A'], ['H', 'E', 'B'], ['I', 'F', 'C']])
        self.assertEqual(gridPositions, [[(0, 2), (0, 1), (0, 0)], [(1, 2), (1, 1), (1, 0)], [(2, 2), (2, 1), (2, 0)]])

    def testDownRightDiagonalGridGeneration(self):
        # defining this as top left to bottom right
        self.testParser.textToParse = ['youre not the boss of me now', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = self.testReorienter.generateForwardRightDiagonal(self.testParser.generateWordSearchGrid())

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
        self.testParser.textToParse = ['youre not the boss of me now', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = self.testReorienter.generateUpRightDiagonal(self.testParser.generateWordSearchGrid())

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
        self.testParser.textToParse = ['youre not the boss of me now', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = self.testReorienter.generateUpRightDiagonal(self.testParser.generateWordSearchGrid())

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
        self.testParser.textToParse = ['and youre not so big', 'A,B,C', 'D,E,F', 'G,H,I']
        testLetters = self.testReorienter.generateForwardRightDiagonal(self.testParser.generateWordSearchGrid())

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

    def testWordFinderInstance(self):
        testFinder = wordFinder()
        self.assertTrue(testFinder)

    def testWordFindsHorizontalWords(self):
        self.testParser.textToParse = ['BC,DEF,HI', 'A,B,C', 'D,E,F', 'G,H,I']

        targetWords = self.testParser.parseTargetWords()
        testGrid = self.testParser.generateWordSearchGrid()

        self.assertEqual([self.testFinder.findWords(testGrid, targetWord) for targetWord in targetWords],
                         [('BC', [(1, 0), (2, 0)]), ('DEF', [(0, 1), (1, 1), (2, 1)]), ('HI', [(1, 2), (2, 2)])])

    def testWordFindsBackwardsWords(self):
        self.testParser.textToParse = ['ED,IHG', 'A,B,C', 'D,E,F', 'G,H,I']

        targetWords = self.testParser.parseTargetWords()
        testGrid = self.testParser.generateWordSearchGrid()
        testGrid = self.testReorienter.generateBackwardHorizontal(testGrid)

        self.assertEqual([self.testFinder.findWords(testGrid, targetWord) for targetWord in targetWords],
                         [('ED', [(1, 1), (0, 1)]), ('IHG', [(2, 2), (1, 2), (0, 2)])])

    def testWordFindsVerticalDownWords(self):
        self.testParser.textToParse = ['BE,CFI', 'A,B,C', 'D,E,F', 'G,H,I']

        targetWords = self.testParser.parseTargetWords()
        testGrid = self.testParser.generateWordSearchGrid()
        testGrid = self.testReorienter.generateForwardVertical(testGrid)

        self.assertEqual([self.testFinder.findWords(testGrid, targetWord) for targetWord in targetWords],
                         [('BE', [(1, 0), (1, 1)]), ('CFI', [(2, 0), (2, 1), (2, 2)])])

    def testWordFindsVerticalUpWords(self):
        self.testParser.textToParse = ['GD,IF', 'A,B,C', 'D,E,F', 'G,H,I']

        targetWords = self.testParser.parseTargetWords()
        testGrid = self.testParser.generateWordSearchGrid()
        testGrid = self.testReorienter.generateBackwardVertical(testGrid)

        self.assertEqual([self.testFinder.findWords(testGrid, targetWord) for targetWord in targetWords],
                         [('GD', [(0, 2), (0, 1)]), ('IF', [(2, 2), (2, 1)])])

    def testWordFindsDiagonalDownRightWords(self):
        self.testParser.textToParse = ['BF,DH', 'A,B,C', 'D,E,F', 'G,H,I']

        targetWords = self.testParser.parseTargetWords()
        testGrid = self.testParser.generateWordSearchGrid()
        testGrid = self.testReorienter.generateForwardRightDiagonal(testGrid)

        self.assertEqual([self.testFinder.findWords(testGrid, targetWord) for targetWord in targetWords],
                         [('BF', [(1, 0), (2, 1)]), ('DH', [(0, 1), (1, 2)])])

    def testWordFindsDiagonalUpRightWords(self):
        self.testParser.textToParse = ['DB,HF', 'A,B,C', 'D,E,F', 'G,H,I']

        targetWords = self.testParser.parseTargetWords()
        testGrid = self.testParser.generateWordSearchGrid()
        testGrid = self.testReorienter.generateUpRightDiagonal(testGrid)

        self.assertEqual([self.testFinder.findWords(testGrid, targetWord) for targetWord in targetWords],
                         [('DB', [(0, 1), (1, 0)]), ('HF', [(1, 2), (2, 1)])])

    def testWordsFindsDiagonalUpLeftWords(self):
        self.testParser.textToParse = ['HD,FB', 'A,B,C', 'D,E,F', 'G,H,I']

        targetWords = self.testParser.parseTargetWords()
        testGrid = self.testParser.generateWordSearchGrid()
        testGrid = self.testReorienter.generateForwardRightDiagonal(testGrid)
        testGrid = [row[::-1] for row in testGrid]

        self.assertEqual([self.testFinder.findWords(testGrid, targetWord) for targetWord in targetWords],
                         [('HD', [(1, 2), (0, 1)]), ('FB', [(2, 1), (1, 0)])])

    def testWordFindsDiagonalDownLeftWords(self):
        self.testParser.textToParse = ['BD,CEG', 'A,B,C', 'D,E,F', 'G,H,I']

        targetWords = self.testParser.parseTargetWords()
        testGrid = self.testParser.generateWordSearchGrid()
        testGrid = self.testReorienter.generateUpRightDiagonal(testGrid)
        testGrid = [row[::-1] for row in testGrid]

        self.assertEqual([self.testFinder.findWords(testGrid, targetWord) for targetWord in targetWords],
                         [('BD', [(1, 0), (0, 1)]), ('CEG', [(2, 0), (1, 1), (0, 2)])])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        WordSearchTests.testFile = sys.argv.pop()
    unittest.main()
