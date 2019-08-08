# WordSearcher
accenture word search kata

##### Instructions to run:
1. download repo to a local directory
2. fom the command line, invoke either the WordSearchMain.py or WordSearchTests.py files as follows:
2a. to run the program: 

`python (directory path)/WordSearchMain.py (file path to target input file)`
   
   e.g.: 
  
`python C://users/yourname/wordSearcher/WordSearchMain.py C://users/yourname/wordSearcher/input.txt`
  
   2b. to run the test suite: 
  
`python <directory path>/WordSearchTests.py <test input file>`

   e.g.: 
      
`python C://users/yourname/wordSearcher/WordSearchTests.py C://users/yourname/wordSearcher/testInput.txt`
  
   or: 
        
`python C://users/yourname/wordSearcher/WordSearchTests.py -v C://users/yourname/wordSearcher/testInput.txt`
  
testInput is the provided input file, it's only used to test file reading functionality

##### Description
given an input file of the form of a single line of target words, separated by commas, followed by an n x n square grid of letters separated by commas,
this program will find each word and report its coordinates to the command line in the format e.g.:

  `WORD: (0,1),(0,2),(0,3),(0,4)`

for each target word in the input file.
