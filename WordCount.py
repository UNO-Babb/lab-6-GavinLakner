#WordCount.py
#Name: Gavin Lakner
#Date: 10/5/2025
#Assignment: Word Count

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    letters = line.split() #don't know what to split it by
    for w in words:
      wordCount = wordCount + 1 
    for l in letters:
      letterCount = letterCount + 1

  print("Lines:" , lineCount)
  print("Words:" , wordCount)
  print("Letters:" , letterCount)
#nothing in notes or lecture over how to find individual letter count and 
#google wants me to add a 10 lines of code for it so idk

if __name__ == '__main__':
  main()
