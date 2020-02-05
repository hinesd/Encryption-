# -*- coding: utf-8 -*-

#iostream

import sys

def Encrypt(key, file):
    #check for key and file
    if isinstance(key, str) and isinstance(file, str):
        #create array of words
        f = open(file)
        text = f.readlines()
        stringList = []
        newLine = []
        chopLine = []
        for x in text:
            stringList.append(x)
        print(stringList)
        for x in stringList:
            line =  list(x)
            for y in line:
                if(y.isalpha()): 
                    newLine.append(y.upper())
                else:
                    newLine.append(y)
        print(newLine)
        i = 0
        while i < (len(newLine)-1):
            if(newLine[i].isalpha() and newLine[i+1].isalpha()):
                    chopLine.append(newLine[i] + newLine[i+1])
                    i += 2
            else:
                chopLine.append(newLine[i])
                i += 1
        print(chopLine)
        #create key
        keyTable = makeKey(key)
        print(keyTable)
        #create empty coded text string
        codedText = ""     
        for j in chopLine:
            if(len(j) == 2):
                row1, col1 = divmod(keyTable.index(j[0]), 5)
                row2, col2 = divmod(keyTable.index(j[1]), 5)

                if row1 == row2:
                    codedText += keyTable[row1*5+(col1-1)%5]
                    codedText += keyTable[row2*5+(col2-1)%5]
                elif col1 == col2:
                    codedText += keyTable[((row1-1)%5)*5+col1]
                    codedText += keyTable[((row2-1)%5)*5+col2]
                else: # rectangle
                    codedText += keyTable[row1*5+col2]
                    codedText += keyTable[row2*5+col1]
            else:
                codedText+=j
        print(codedText)
    else:
    	print("give me a key and then the name of your file ")

def makeKey(key):
    keyTable = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in key.upper():
        if char not in keyTable and char in alphabet:
            keyTable.append(char)
    for char in alphabet:
        if char not in keyTable:
            keyTable.append(char)
    return keyTable

Encrypt(sys.argv[1],sys.argv[2])
