import random as r
result = []
s = 0
while s < 4:
    yangi_kod = r.randint(1,4)
    s +=1
    while yangi_kod in result:
        yangi_kod = r.randint(1,4)
    result.append(yangi_kod)
print(result)

k = 0 
print("Uchta urinishda toping")
while k < 3: 
    bir = int(input("birinchi son kiritng: ")) 
    ikki = int(input("ikkinchi soni kiriting : ")) 
    uch = int(input("Uchinchi soni kiriting: ")) 
    turt = int(input("Turtinchi soni kiriting: ")) 
    if bir == result[0]: 
        print("\nBirinchisi tugri\n")
    else: 
        print("\nBirinchisida xato bor\n") 
    if ikki == result[1]: 
        print("Ikkinchisi tugri\n")
    else: 
        print("Ikkinchisida xato bor\n") 
    if uch == result[2]: 
        print("Uchinchi tugri\n")
    else: 
        print("Uchinchida xato bor\n") 
    if turt == result[3]: 
        print("turtinchi tugri\n")
    else: 
        print("turtinchi xato bor\n") 
    k +=1   
    if bir == result[0] and ikki == result[1] and uch == result[2] and turt == result[3]:
        print("\n\n Siz Topdingiz\n\n")
    else:
        print(f"\nUrinishlar soni : {k}  !!!\n")
k +=1
print(f"\n\nSiz {k} urinishda topdingiz")
print("_______   _________   _________    __  ")
print("|     |   |       |   |       |    |   --")
print("|         |       |   |       |    |     --")
print("|         |       |   |       |    |       |")
print("|   ---   |       |   |       |    |     --")
print("|      |  |       |   |       |    |   --")
print(" -------  ---------   ---------    --  ")
print("")
print("")
print("")
print("")


        
