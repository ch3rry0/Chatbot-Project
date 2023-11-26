import os

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

def lowercase():
    #Converts all text files to lowercase
    try:
        os.mkdir('clean')
    except FileExistsError:
        pass
    A = os.listdir('speeches')
    for i in range(len(A)):
        with open(f'speeches/{A[i]}', 'r+', encoding='utf-8') as file:
            data = file.read()
            new = open(f'clean/{A[i]}', 'w+', encoding='utf-8')
            new.write(data.lower())
lowercase()