from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    kortingsprijs=prijs*(1-korting)
    aanbieding_tekst_1=f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {kortingsprijs}0"
    aanbieding_tekst_1_1=aanbieding_tekst_1[:90]
    print(aanbieding_tekst_1_1,"euro.")
    #Om ervoor te zorgen dat het bedrag in twee decimalen wordt uitgedrukt ondanks de prijs en het kortingspercentage heb ik de string van de aanbiedingstekst in twee delen gemaakt die in regel 8 samengevoegd worden.
aanbieding_1("aardbei", 4, 0.1)

print()

def inkomsten_totaal(inkomsten,btw):
    totaal=sum(inkomsten)
    float(btw)
    bedrag=totaal*btw
    inkomsten_totaal_tekst_1=f"Het totaal van alle inkomsten deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    print(inkomsten_totaal_tekst_1)
inkomsten_totaal((220,430,125,160,205,90,345),0.09)

print()

mijn_lijst=[220, 430, 125, 160, 205, 90, 345]
def laag_en_hoog(mijn_lijst):
    mijn_lijst.sort()
    laag=mijn_lijst[0]
    hoog=mijn_lijst[-1]
    return([hoog, laag])
print(laag_en_hoog(mijn_lijst))

print()

def gemiddelde(mijn_lijst):
    bedrag=(sum(mijn_lijst))/len(mijn_lijst)
    gemiddelde_tekst=f"De gemiddelde inkomsten deze week zijn {bedrag} euro"
    return(gemiddelde_tekst)
print(gemiddelde(mijn_lijst))

print()

invoer_lijst=[10,5,3,2,1,2,9]
def meervoudig(invoer_lijst):
    return(laag_en_hoog(invoer_lijst))
print (meervoudig(invoer_lijst))

print()

def combinatie(invoer_lijst_2):
    korte_lijst=meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)

#Bij de laatste opgave van het huiswerk van les 8 (regels 48 t/m 50) vond ik het vrij lastig om te weten wat ik aan het doen was. Het lukte mij ook niet om een uitvoer te creëren zodat ik mijn code kon controleren.
