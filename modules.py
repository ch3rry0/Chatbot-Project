from os import *

def extract_names(filename):
    """Extracts the name of the file"""
    f = filename.split('speeches/Nomination_')
    if f[1][6] == '1':
        f[1].split('1.txt')
        return str(f[1])
    elif f[0][6] == '2':
        return str(f.split('2.txt'))
    else:
        return str(f.split('.txt'))
    
f = extract_names('speeches/Nomination_Chirac1.txt')
print(f)