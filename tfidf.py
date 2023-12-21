from math import log10
import os
import re

def tf(filename:str) -> dict: #Takes a file and returns the TF score for each word 
    Lwords = []
    with open(filename, 'r+', encoding='utf-8') as f:
        for line in f:
            for word in re.split('[!;:` 0 1 2 3 4 5 6 7 8 9 -.,\' \n]', line):
                Lwords.append(word)
    tfscore = {}
    for elem in Lwords:
        if elem in tfscore:
            tfscore[elem] += 1
        else:
            tfscore[elem] = 1
    return tfscore

def idf(folder:str) -> dict: #Takes a folder and returns the IDF score for each word
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

def matrix(folder:str) -> list:
    M = []
    idfscore = idf(folder)
    dirlist = os.listdir(folder)
    for k in range(len(dirlist)):
        tfscore = tf(f'{folder}/{dirlist[k]}')
        for elem in tfscore:
            temp = []
            temp.append(elem)
            for _ in range(len(dirlist)):
                temp.append(idfscore[elem] * tfscore[elem])
            if temp in M:
                M.remove(temp)
            M.append(temp)
    return M
"""
Mat = matrix('clean')
for k in range(len(Mat)):
    print(f'{Mat[k][0]} : {Mat[k][1]}, {Mat[k][2]}, {Mat[k][3]}, {Mat[k][4]}, {Mat[k][5]}, {Mat[k][6]}, {Mat[k][7]}, {Mat[k][8]}')
"""