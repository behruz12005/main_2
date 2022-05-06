import random
list1 = ["qogoz","qaychi","tosh"]
randomm = random.choice(list1)
sen = 0
kam = 0
natija = 0
while natija <= 5:
    son = str(input("(qogoz) and (qaychi) and (tosh):  "))
    if son == "no":
        break
    else:
        if son == "qaychi" and randomm == "qaychi" or son == "qogoz" and randomm == "qogoz" or son == "tosh" and randomm == "tosh":
            print(f"{son.upper()}  =  {randomm.upper()}")
            print("durang")
        elif son == "qogoz" and randomm == "qaychi" or son == "qaychi" and randomm == "tosh" or son == "tosh" and randomm == "qogoz":
            print(f"{son.upper()}  <  {randomm.upper()}")
            print("Yutqazdiz") 
            kam+=1
        elif son == "qaychi" and randomm == "qogoz" or son == "tosh" and randomm == "qaychi" or son == "qogoz" and randomm == "tosh":
            print(f"{son.upper()}  >  {randomm.upper()}")
            print("Yutingiz")
            sen+=1
    natija +=1
if sen > kam:
    print(f"Bu uyinda {sen} achko bilan yutingiz")
elif sen< kam:
    print(f"bu uyinda {kam} achko bilan kam yuti")
else:
    print("Bu uyinda durang")