def presenteer(mijn_dict, totaal):
    for k,v in mijn_dict.items():
        print(k," : ",v, "euro")
    print("="*26)
    print("totaal :",totaal,"euro")

#Uitvoer volgens het voorbeeld:
presenteer({"vis":10,"vlees":25,"overig":15},50)