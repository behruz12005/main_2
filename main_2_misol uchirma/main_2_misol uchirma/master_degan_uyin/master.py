from pickle import FALSE 
import random as r 
from re import T 
print("O'yindi boshladik") 
print("uyinn haqida: 4 ta raqam kirgiz agar men kirgiz raqamlar bilan seni raqamlaring teng bulsa yutasan bulm,asa....") 
s = 0 
ishora = True 
ishora1 = True 
ishora2 = True 
while s < 1: 
    b = r.randint(1,4) 
    print(b) 
    i = r.randint(1,4) 
    while ishora: 
        if i != b: 
            print(i) 
            ishora = False 
        else: 
            i = r.randint(1,4) 
            ishora = True 
    u = r.randint(1,4) 
    while ishora1: 
        if u != b and u != i: 
            print(u) 
            ishora1 = False 
        else: 
            u = r.randint(1,4) 
            ishora1 = True 
    t = r.randint(1,4) 
    while ishora2: 
        if t != b and t != i and t != u: 
            print(t) 
            ishora2 = False 
        else: 
            u = r.randint(1,4) 
            ishora2 = True 
    s +=1 
 
# bu yerda random tugadi 
k = 0 
while k < 5: 
    bir = int(input("birinchi son kiritng: ")) 
    ikki = int(input("ikkinchi soni kiriting : ")) 
    uch = int(input("Uchinchi soni kiriting: ")) 
    turt = int(input("Turtinchi soni kiriting: ")) 
    if bir == b and ikki == i and uch == u and turt == t: 
        print("Siz topdingiz") 
        break 
    else: 
        print("Notugri") 
        k +=1 
print(f"Siz {k} urinishda topdingiz")