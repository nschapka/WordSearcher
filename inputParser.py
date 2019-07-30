class inputParser:

    def __init__(self):
        pass

    def getTextToParse(self, inputReader):
        self.textToParse = inputReader.inputText

    def parseTargetWords(self):
        targetWords = str.split(self.textToParse[0], ',')
        return targetWords
