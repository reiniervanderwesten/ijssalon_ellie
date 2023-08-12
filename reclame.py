def aanbieding_1(smaak, prijs, korting):
    
    print(f"vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {((1-korting)* prijs)} euro.")
    


aanbieding_1("aardbei", 4, 0.1)

def inkomsten_totaal(inkomsten):
    totaal=0
    for nr in inkomsten:
        totaal+=nr
    
    return totaal

print(inkomsten_totaal([220, 430, 125, 160,205,90,345]))