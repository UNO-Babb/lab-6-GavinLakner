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
    letters = words.split()
    for w in words:
      wordCount = wordCount + 1
      for l in letters:
        letterCount = letterCount + 1
  

  print("Lines:" , lineCount)
  print("Words:" , wordCount)
  print("Letters:" , letterCount)


if __name__ == '__main__':
  main()
