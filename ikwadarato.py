while True:
    ma_chaine = ''
    n = int(input("Entrez le nombre de fois que vous voulez que * apparaisse: "))
    m = n - 2
    ma_chaine = '* '+'* '*m +'*'
    ma_chaine_y = '*'+ ' '*(2*m+1) + '*'

    print(ma_chaine)
    i=0
    while i<m :
        print(ma_chaine_y)
        i +=1
    print(ma_chaine)