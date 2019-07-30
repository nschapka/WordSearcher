import unittest
from inputReader import inputReader

class WordSearchTests(unittest.TestCase):

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
            self.assertTrue(inputText)  # at this point i just want to check that there is text read - don't care if the input is valid
        finally:
            fileObject.close()


if __name__ == '__main__':
    unittest.main()
