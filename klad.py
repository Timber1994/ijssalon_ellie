from reclame import laag_en_hoog
from algemene_functies import mijn_functie_2

invoer_lijst=[10,5,3,2,1,2,9]
def meervoudig(invoer_lijst):
    return(laag_en_hoog(invoer_lijst))
print (meervoudig(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst=meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)

    







    
    #inkomsten=[220, 430, 125, 160, 205, 90, 345]
    #totaal=sum(inkomsten)
    #btw=0.09
    #bedrag=totaal*btw
    #inkomsten_totaal_tekst_1=f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    #print(inkomsten_totaal_tekst_1)
#print(inkomsten_totaal())