#WordIndex.py
#Name: Gavin Lakner
#Date: 10/5/2025
#Assignment: WordIndex

def main():
  textFile = open("fish.txt", 'r')
  
  words = {}
  lineNum = 0

  for line in textFile:
    lineNum = lineNum + 1
    wordList = line.split()
    for w in wordList:
      w = w.lower()
      w = w.replace("," , "")
      w= w.replace("!", "")
      w= w.replace(".", "")
  
      if w in words:
        if lineNum not in words[w]:
         words [w].append (lineNum)
      else:
         words[w] = [lineNum]

  for word in words:
   print(word, words[word])


if __name__ == '__main__':
  main()
