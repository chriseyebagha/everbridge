import re
import io
import sys
import glob
import os

replaceWith = "202-221-1414"
path = '/var/www'
content=[]

def parser():
  for filename in glob.glob(os.path.join(path, '*.html')):
    #Open File
    with open( filename, 'r+') as usersFile:
      eachLines = usersFile.readlines()

      # reads each thisLine in the file
      for line in eachLines:
          thisLine = line
          #Do regular Expression
          rgxpattern= "(\W\d[-\.\s]??\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\W\d[-\.\s]??\d{3}[-\.\s]??\w{3}[-\.\s]??\w{4}|\d{3}[-\.\s]??\w{3}[-\.\s]??\w{4}|\(\d{3}\)\s*\w{3}[-\.\s]??\w{4}|\d{3}[-\.\s]??\w{4})"
          regexp = re.compile(rgxpattern, re.VERBOSE)

          if regexp.findall(thisLine):
            for groups in regexp.findall(thisLine):
              # Subtitute string variable
              thisLine = thisLine.replace(groups, replaceWith)
          else:
            pass

          # Append Each Line to an array variable
          content.append(thisLine)
      usersFile.close()
      print(content)

      #Write to the original file
      writeToFile(content, filename)


def writeToFile(content, filename):
   with open(filename, 'w+') as usersFile:
      for line in content:
        usersFile.write(line)
   usersFile.close()


if __name__=="__main__":
    parser()

