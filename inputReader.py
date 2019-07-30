class inputReader:

    def __init__(self, filePath):
        self.filePath = filePath

    def readText(self, file):
        self.inputText = []
        for line in file:
            self.inputText.append(line)

        return self.inputText