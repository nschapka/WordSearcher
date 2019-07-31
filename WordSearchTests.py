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

        self.assertEqual(wordSearchGrid, [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])

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

    def testWordFinderTestStringsGeneration(self):
        testFinder = wordFinder()
        testGrid = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

        self.assertEqual(testFinder.generateForwardHorizontal(testGrid), ['ABC', 'DEF', 'GHI'])
        self.assertEqual(testFinder.generateBackwardHorizontal(testGrid), ['CBA', 'FED', 'IHG'])
        self.assertEqual(testFinder.generateForwardVertical(testGrid), ['ADG', 'BEH', 'CFI'])
        self.assertEqual(testFinder.generateBackwardVertical(testGrid), ['GDA', 'HEB', 'IFC'])



if __name__ == '__main__':
    unittest.main()
