from definition import *

# Na riesenie pouzi funkcie:
#     dopredu(vzdialenost o kolko)
#         priklad: dopredu(100) -->pohne sa dopredu 100 pixelov
        
#     vlavo(uhol otocenia v stupnoch)
#         priklad: vlavo(90) --> otoci sa vlavo o 90 stupnov
        
#     vpravo(uhol otocenia v stupnoch)
#         priklad: vpravo(90) --> otoci sa vprao o 90 stupnov
        
#     opakuj(kolko krat, o aky uhol, aka vzdialenost)
#         priklad: opakuj(8,360/8,50) ---> vytvori 8-uholnik s dlzkou steny 50
            # preco 360/8 ? --> chceme vytvorit 8-uholnik, cize tam kde zacneme sa chceme aj vratit,teda vytvorime akysi hranaty kruh, 
            # lebo bude mat 8 stran, ale ked sa otacame okolo niecoho tak sa otocime o 360 stupnov ak sa vratime na to iste miesto, 
            # preto tu vzdialenost rozdelime na 8 casti a cize aj ten uhol musime rozdelit na 8 casti, takze 360/8
    

# riesenie cislo 3, vyuzivanie vlastnych definicii
vpravo(20)
dopredu(270)
vlavo(110)
dopredu(100)
opakuj(19,-360/32,50)
vpravo(120)
dopredu(120)
vpravo(80)
opakuj(10,360/80,50)
vlavo(90)
dopredu(60)
vlavo(80)
opakuj(7,-360/110,50)
vpravo(90)
dopredu(80)


# potrebne, aby obrazovka zostala otvorena 
screen.mainloop()
