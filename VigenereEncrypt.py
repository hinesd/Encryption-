# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:21:13 2020

@author: Dillons PC
"""
## this is just an edit

import sys

def Encrypt(key, file):
    counter = 0
    if isinstance(key, str) and isinstance(file, str):
            f = open(file)
            text = f.readlines()
            newList = []
            for x in text:
                line = list(x)
                for i in line:
                    print("plaintext: "+i)
                    if(i.isalpha()):
                        if(i.isupper()):
                            plaintext = ord(i) - ord('A')
                            keytext = ord(key[counter%len(key)]) - ord('A')
                            newList.append( chr(((plaintext + keytext)%26) + ord('A')) )
                        else:
                            plaintext = ord(i) - ord('a')
                            keytext = ord(key[counter%len(key)]) - ord('a')
                            newList.append( chr(((plaintext + keytext)%26) + ord('a')) )
                            
                    else:
                        newList.append(i)
                    counter += 1
                    
                f = open("VigenereEncrypted.txt", "w" )
                for i in newList:
                    f.write(i)
            
                
                
    else : 
        print("give me a string that will be your key and then the name of your file ")


Encrypt(sys.argv[1],sys.argv[2])