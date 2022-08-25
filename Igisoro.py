# FONCTION YO GUKORA IGISORO
def igisoro_co_kugwiza ():

        i = 1
        while i < 13:
            ico_dutora = gusohoka * i
            print(str(i) + " x " + str(gusohoka) + " = " + str(ico_dutora))
            i += 1

# KUBWIRA UMUKIRIYA INGENE APPLICATION IKORA
print('SHIRAMWO IGIHARURO TUCE TUGUHA IGISORO CACO')
print('KUGIRA MUSOHOKE ANDIKA UBUSA (O)')
# KUMUSABA GUSHIRAMWO IGIHARURO
gusohoka = int(input('USHAKA IGISORO CA KANGAHE:'))
while gusohoka != 0:
    igisoro_co_kugwiza()
    gusohoka = int(input('KURABA IKINDI GISORO CA: '))

print("mwakoze kugerageza, tuzosubira")