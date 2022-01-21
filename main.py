'''
2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! 
A program tartalmazza a függvény hívását is!
'''

lista = [3, 3, 3, 6, 3]

def paros_e(listak):
    gep = 0
    while gep == 0:
        for i in listak:
            if i % 2 == 0:
                return print(True)
            else:
                gep = 2
    else:
        return print(False)
        
paros_e(lista)
