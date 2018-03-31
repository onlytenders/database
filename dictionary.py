personInfo = {'lol':'kek',
                          'kek':'lol',
                          'lolkek':'keklol',
                          'keklol':'lolkek'}
lolilikek = input('lol or kek? ')
lolilikek = lolilikek.lower()
try:
    print(personInfo[lolilikek])
except:
    print('i ne lol i ne kek')
