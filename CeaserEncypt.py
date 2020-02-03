# -*- coding: utf-8 -*-

#iostream

import sys

## this in an edit
def Encrypt(shift, file):
    if isinstance(shift, int) and isinstance(file, str):
            f = open(file)
            text = f.readlines()
            stringList = []
            newLine = []
            for x in text:
                stringList.append(x)
            print(stringList)
            for x in stringList:
                line =  list(x)
                for y in line:
                    if(y.isalpha()): 
                        newLine.append(chr(ord(y) + shift))
                    else:
                        newLine.append(y)
            print(newLine)
            f = open("ceaserEncrypted.txt", "w" )
            for i in newLine:
                f.write(i)
                
                
    else : 
        print("give me an int and then the name of your file ")

Encrypt(int(sys.argv[1]),sys.argv[2])

    