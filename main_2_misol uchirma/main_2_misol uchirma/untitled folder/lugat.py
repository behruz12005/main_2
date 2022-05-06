til = str(input("tilni kiting(en/uz): "))
suz = str(input("So'z kiritng: "))
if til == "en":
    lugat_en = { "apple":"olma","red":"qizil","banana":"banan","phone":"telfon","eyebrow":"qosh","bag":"sumka","pensil":"qalam","elephant":"fil","cat":"mushuk","yellow":"sariq"}
    for i in lugat_en:
        if suz != i:
            print("Bunaqa suz yuq")
            break
        else:
            print(lugat_en[f"{suz}"])
elif til == "uz":
    lugat_uz = {"olma":"apple","qizil":"red","banan":"banan","telfon":"phone","qosh":"eyebrow","sumka":"bag","qalam":"pensil","fil":"elephant","mushuk":"cat","sariq":"yellow"}
    for i in lugat_uz:
        if suz != i:
            print("Bunaqa suz yuq")
            break
        else:
            print(lugat_uz[f"{suz}"])
else:
    print("Unaqa til yuq")