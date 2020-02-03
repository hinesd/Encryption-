# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:15:33 2020

@author: Dillons PC
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:10:15 2020

@author: Dillons PC
"""

import sys



def Decrypt(cypher, file):  
    if len(cypher) == 26 and cypher.isalpha() and isinstance(file, str):
        print(alphabet)
        f = open(file)
        text = f.readlines()
        line = []
        newLine = []
        for x in text:
            line = list(x)
            for y in line:
                if(y.isalpha()):
                    newLine.append(cypher[ord(y.lower()) % ord('a')])
                else:
                    newLine.append(y)
            f = open("MonoDecrypted.txt", "w" )
            for i in newLine:
                f.write(i)
                
            print(line)
            print(newLine)
                
    else: 
        print("give me a permutaion of the alphabet and then the name of your file ")
    
alphabet = []
for x in range(0,26):
    alphabet.append(chr(ord('a') + x))
Decrypt(sys.argv[1],sys.argv[2])
##zyxwvutsrqponmlkjihgfedcba