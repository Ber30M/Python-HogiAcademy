print("DUKORE IKWADARATO \nSHIRAMWO IGIHARURO KINGANA N'URUHANDE RW'INO KWADARATO")
while True:
    ma_chaine = ''
    n = int(input("Igiharuro: "))
    m = n - 2
    ma_chaine = '* '+'* '*m +'*'
    ma_chaine_y = '*'+ ' '*(2*m+1) + '*'

    print(ma_chaine)
    i=0
    while i<m :
        print(ma_chaine_y)
        i +=1
    print(ma_chaine)