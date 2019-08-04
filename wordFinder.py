import re
from letter import letter

class wordFinder:
    def __init__(self):
        pass

    def __generateTestStrings(self, testGrid):
        testStrings = []
        for row in testGrid:
            testStrings.append("".join([letter.char for letter in row]))

        return testStrings

    def findWords(self, searchGrid, targetWords):
        # the output takes the form of a list of tuples, composed of the found word and a list of letter coordinates
        foundWords = []
        testStrings = self.__generateTestStrings(searchGrid)

        for target in targetWords:
            for row in range(len(testStrings)):
                match = re.search(target, testStrings[row])
                if match:
                    # collate the target word with the positions of its letters, sliced from the search grid with the regex match bounds
                    foundWords.append((target, [letter.position for letter in searchGrid[row][match.start():match.end()]]))
                    break

        return foundWords


