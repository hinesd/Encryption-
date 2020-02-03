# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:10:15 2020

@author: Dillons PC
"""

import sys



def Encrypt(cypher, file):  
    if len(cypher) == 26 and isinstance(file, str):
        print(alphabet)
        f = open(file)
        text = f.readlines()
        line = []
        newLine = []
        for x in text:
            line = list(x)
            print(ord('t')% ord('a') + 1)
            for y in line:
                if(y.isalpha()):
                    newLine.append(cypher[ord(y.lower()) % ord('a')])
                else:
                    newLine.append(y)
            f = open("MonoEncrypted.txt", "w" )
            for i in newLine:
                f.write(i)
                
            print(line)
            print(newLine)
        
                
    else: 
        print("give me a permutaion of the alphabet and then the name of your file ")
    
alphabet = []
for x in range(0,26):
    alphabet.append(chr(ord('a') + x))
    
Encrypt(sys.argv[1],sys.argv[2])
##zyxwvutsrqponmlkjihgfedcba