"""
FileName = PythonTableModule.py

TODO:
  *Center the values in the fields
  *Change variable names to production names
"""

def createAndPrintTable(headerValueList,fieldValueList):
    headerList = headerValueList
    sampleList = fieldValueList
       
    midStr = "" #midStr holds the formated contents of the list
    numOfCol = len(headerList) - 1 #Desired number of colomns
    colCount = 1 #Keeps track of how many colomns are generated
    rowCount = 1 #Keeps track of how many rows are generated
    valCount = 0 #Keeps track of how many values are added to midStr
    maxLen = 0 #Holds the value of the longest value in terms of characters

    for index in range(len(sampleList)): #Iterate through the list
      currLen = len(str(sampleList[index])) #Length of the current value string
      if currLen > maxLen: #Finds the length of the longest value string
        maxLen = currLen

    for index in range(len(headerList)): #Iterate through the header list
      currLen = len(str(headerList[index])) #Length of the current header string
      if currLen > maxLen: #Finds the length of the longest header string
        maxLen = currLen

    for index in range(len(sampleList)): #Iterate through the list
      currLen = len(str(sampleList[index])) #Length if the curent value string
      currStr = str(sampleList[index]) #Holds the current value string

      if currLen != maxLen: #Adds spaces such that all value strings are the same length
        for index in range(maxLen-currLen):
          currStr = currStr + ' '

      if colCount - 1 != numOfCol + 1: #If not ever value has been added to this row
        if index != len(sampleList): #If all values have not been iterated
          midStr += "| {} "

      if colCount == numOfCol + 1: #If the number of columns in this row is equal to the number of desired columns
        midStr += "|" +'\n'
        rowCount += 1
        colCount = 0

      midStr = midStr.format(currStr) #Format our current field with its associated value

      colCount += 1
      valCount += 1

    if valCount != (numOfCol * rowCount): # This mean there are empty fields
      for index in range((numOfCol + 1) * rowCount - valCount):
        midStr += "|  "
        for index in range(maxLen):
          midStr += " "
      midStr += "|"
    topAndBotStr = ""

    splitMidStr = midStr.split('\n')
    displayList = []

    for line in splitMidStr:
      if line != '': #Ensure there are no blank lines
        displayList.append(line)

    for index in range(len(splitMidStr[0])): #Create lower boarders for fields
      topAndBotStr += "-"

    for index in range(len(headerList)): #Iterate through headerList
      currHeaderLen = len(headerList[index]) #Holds length of the current header string
      print("| " + str(headerList[index]),end=' ')#Prints the header with a | in front
      for index in range(maxLen - currHeaderLen): #Loops if the current header string is not the same as max length
        print(" ",end='') #Prints paddings
    print("|") #Prints ending |

    print(topAndBotStr) #Print top border
    for line in displayList:
      if line[2] == ' ':
        pass
      else:
        print(line) #Print fields
        print(topAndBotStr) #Print bottom field borders
