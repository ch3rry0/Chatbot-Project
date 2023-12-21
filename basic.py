import os
import tfidf

def extract_names(filename:str) -> str:
    #This function extracts the names of the Presidents from the files
    if 'speeches' in filename:
        f = filename.split('speeches/Nomination_')
    else:
        f = filename.split('Nomination_')
    if '1' in f[1]:
        a = f[1].split('1.txt')
        return str(a[0])
    elif '2' in f[1]:
        a = f[1].split('2.txt')
        return str(a[0])
    else:
        a = f[1].split('.txt')
        return str(a[0])
    
def list_names(folder:str) -> list:
    #List all the names of the presidents and returns them as a list
    L = []
    A = os.listdir(folder)
    for k in range(len(A)):
        if extract_names(A[k]) not in L:
            L.append(extract_names(A[k]))
    return L

def lowercase(): #Converts all text files to lowercase
    #Tries to create directory 'clean'. If it already exists then pass
    try:
        os.mkdir('clean')
    except FileExistsError:
        pass
    A = os.listdir('speeches')
    #We create a loop to go through each file, then copy its content and paste it in lowercase in a new file
    for i in range(len(A)):
        with open(f'speeches/{A[i]}', 'r+', encoding='utf-8') as file:
            data = file.read()
            new = open(f'clean/{A[i]}', 'w+', encoding='utf-8')
            new.write(data.lower())

lowercase()

def unimportant(folder:str):
    matrice = tfidf.matrix(folder)
    print('The most unimportant words are')
    for k in range(len(matrice)):
        if matrice[k][1] == 0 and matrice[k][2] == 0 and matrice[k][3] == 0 and matrice[k][4] == 0 and matrice[k][5] == 0 and matrice[k][6] == 0 and matrice[k][7] == 0 and matrice[k][8] == 0:
            print(matrice[k][0])

def important(tfidfscore:float, folder:str):
    matrice = tfidf.matrix(folder)
    print('The most important words are')
    for k in range(len(matrice)):
        if matrice[k][1] >= tfidfscore and matrice[k][2] >= tfidfscore and matrice[k][3] >= tfidfscore and matrice[k][4] >= tfidfscore and matrice[k][5] >= tfidfscore and matrice[k][6] >= tfidfscore and matrice[k][7] >= tfidfscore and matrice[k][8] >= tfidfscore:
            print(matrice[k][0])

def most_repeated(n:int, tf_mini:float):
    print(f'The most repeated words by President {extract_names(f'clean/{os.listdir('clean')[n]}')} are : ')
    matrice = tfidf.tf(f'clean/{os.listdir('clean')[n]}')
    for elem in matrice:
        if matrice[elem] > tf_mini:
            print(elem)

def most_rare(idf_mini:float):
    print('The most rare words in the corpus are :')
    idfscore = tfidf.idf('clean')
    for k in idfscore:
        if idfscore[k]*100 > idf_mini:
            print(k)
