def aanbieding_1(smaak, prijs, korting):
    
    print(f"vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {((1-korting)* prijs)} euro.")
    


aanbieding_1("aardbei", 4, 0.1)

print()

def inkomsten_totaal(inkomsten, btw):
    totaal=0
    for nr in inkomsten:
        totaal+=nr
    
    bedrag=btw*totaal
    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")

inkomsten_totaal([220, 430, 125, 160,205,90,345], 0.09)

print()

def laag_en_hoog(mijn_lijst):
    c=max(mijn_lijst)
    d=min(mijn_lijst)
    print([c,d])

    

laag_en_hoog([220,430, 125, 160, 205, 90, 345])

print()

def gemiddelde(mijn_lijst):
    som=sum(mijn_lijst)
    gemiddeld=som/len(mijn_lijst)
    
    print( f"De gemiddelde inkomsten deze week zijn {gemiddeld} euro.")

gemiddelde([220,430,125,160, 205, 90, 345])

def meervoudig(invoer_lijst):
     laag_en_hoog(invoer_lijst)

print(meervoudig([10,5,3,2,1,2,9]))