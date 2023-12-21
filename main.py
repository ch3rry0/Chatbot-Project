import os
import basic
import tfidf

main = True

while main:
    print('Welcome to the python Chatbot', '\n', 'Here are your options :', '\n')
    print('1. List the names of the presidents, type : lst')
    print('2. The most repeated words in the corpus, type : freq')
    print('3. The most rare words in the corpus, type : rare')
    print('4. The idf score of a certain word, type : idf')
    print('5. The tf score of a certain word, type : tf')
    print('6. The TF-IDF score of a certain word, type : tfidf')
    print('7. The most unimportant words, type : unim')
    print('8. The most important words, type : imp')
    I = input()
    if I == 'lst':
        print('The presidents are :')
        for k in range(len(basic.list_names('clean'))):
            print(basic.list_names('clean')[k])
        main = False
    elif I == 'freq':
        print('Choose a text from a President.')
        print('For the 1st Nomination of Chirac, type 1 :')
        print('For the 2nd Nomination of Chirac, type 2 :')
        print('For the Nomination of Giscard d\'Estaing, type 3 :')
        print('For the Nomination of Hollande, type 4 :')
        print('For the Nomination of Macron, type 5 :')
        print('For the 1st Nomination of Mitterrand, type 6 :')
        print('For the 2nd Nomination of Mitterrand, type 7 :')
        print('For the Nomination of Sarkozy, type 8 :')
        try:
            I2 = int(input())
            basic.most_repeated(I2, 8)
        except ValueError:
            print('Enter a valid answer !')
        main = False
    elif I == 'rare':
        try:
            I2 = int(input("Enter a rarity score (in %) : "))
            basic.most_rare(I2)
            main = False
        except ValueError:
            print('Enter a valid answer !')
    elif I == 'idf':
        I2 = input('Enter a word : ')
        for elem in tfidf.idf('clean'):
            if I2 == elem:
                print('The idf score of', elem, 'is : ', tfidf.idf('clean')[elem])
                main = False
    elif I == 'tf':
        print('Choose a text from a President.')
        print('For the 1st Nomination of Chirac, type 1 :')
        print('For the 2nd Nomination of Chirac, type 2 :')
        print('For the Nomination of Giscard d\'Estaing, type 3 :')
        print('For the Nomination of Hollande, type 4 :')
        print('For the Nomination of Macron, type 5 :')
        print('For the 1st Nomination of Mitterrand, type 6 :')
        print('For the 2nd Nomination of Mitterrand, type 7 :')
        print('For the Nomination of Sarkozy, type 8 :')
        try:
            I2 = int(input())
            I2b = input('Enter a word : ')
            for elem in tfidf.tf(f'clean/{os.listdir('clean')[I2-1]}'):
                if I2b == elem:
                    print('The Term Freq of ', elem, 'is : ', tfidf.tf(f'clean/{os.listdir('clean')[I2-1]}')[elem])
                    main = False
                else:
                    print('Your word\'s TF is 0')
                    main = False
        except ValueError:
            print('Enter a valid answer !')
    elif I == 'tfidf':
        I2 = input('Enter a word : ')
        S = 0
        for r in range(len(tfidf.matrix('clean'))):
            if I2 == tfidf.matrix('clean')[r][0]:
                for c in range(1, len(tfidf.matrix('clean')[r])):
                    S += tfidf.matrix('clean')[r][c]
                S = S//8
                print('The TF-IDF score of "',I2,'" is : ', S)
                main = False
    elif I == 'unim':
        basic.unimportant('clean')
        main = False
    elif I == 'imp':
        try:
            I2 = float(input('Enter the TF-IDF score of an important word : '))
            basic.important(I2, 'clean')
            main =  False
        except ValueError:
            print('Enter a valid answer !')
    elif I == "Who is the most handsome President ?":
        print('Chirac of Course !')
    else:
        print('Unvalid answer !')