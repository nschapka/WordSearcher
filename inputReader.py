class inputReader:

    def __init__(self, filePath):
        self.filePath = filePath

    def readText(self, file):
        self.inputText = []
        for line in file:
            self.inputText.append(line.strip())

        if len(self.inputText) < 3:
            raise ValueError('input text not long enough - need at least a line of target words and a 2x2 grid')

        return self.inputText
