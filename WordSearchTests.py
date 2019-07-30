import unittest
from inputReader import inputReader

class WordSearchTests(unittest.TestCase):

    def testInputReaderInit(self):
        testReader = inputReader('C://users/nschapka/desktop/input.txt')
        self.assertEqual(testReader.filePath, 'C://users/nschapka/desktop/input.txt')

    def testInputReaderFindsFile(self):
        testReader = inputReader('C://users/nschapka/desktop/input.txt')
        fileObject = open(testReader.filePath)
        self.assertTrue(fileObject)
        fileObject.close()

if __name__ == '__main__':
    unittest.main()
