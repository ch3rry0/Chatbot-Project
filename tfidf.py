from math import log10
import os
import re

def tf(filename:str) -> dict: #Takes a file and returns the TF score for each word 
    Lwords = []
    with open(filename, 'r+', encoding='utf-8') as f:
        for line in f:
            for word in re.split('[-.,\' \n]', line):
                Lwords.append(word)
    tfscore = {}
    for elem in Lwords:
        if elem in tfscore:
            tfscore[elem] += 1
        else:
            tfscore[elem] = 1
    return tfscore

def idf(folder:str): #Takes a folder and returns the IDF score for each word
    dirlist = os.listdir(folder)
    tempdict = {}
    tempdict2 = {}
    for i in range(len(dirlist)):
        tfscore = tf(f'{folder}/{dirlist[i]}')
        for word in tfscore:
            tempdict[word] = 1
            if word in tempdict2:
                tempdict2[word] += tempdict[word]
            else:
                tempdict2[word] = 1
    idfscore = {}
    for item in tempdict2:
        idfscore[item] = log10(len(dirlist)/tempdict2[item])
    return idfscore

a = True
while a:
    print(idf('clean'))
    b = input('Press any key to kill the program ...')
    if b:
        a = False