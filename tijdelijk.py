prijzen= {"aardbei": 3,
          "vanille": 4,
          "chocolade": 5
         }

aanbieding= 0.8* prijzen["aardbei"]
'''
Aan de docent: in de huiswerkopdracht staat dat ik vanille moet nemen voor de aanbieding. Als ik dit doe krijg ik 3.2 als uitkomst.
Volgens het plaatje bij de huiswerkopdracht moet ik echter 2.4 met veel nullen achter de komma krijgen. 
Dit is wel het geval als ik aardbei kies voor de variabele aanbieding.
Met het oog op het vervolg van de opdracht ga ik daarom uit van aardbei voor de variabele aanbieding. 
'''
reclame_tekst= f"vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}"
reclame_tekst2= reclame_tekst[:63]

reclame_tekst3=reclame_tekst2.upper()
reclame_tekst4=reclame_tekst3.split()

for el in reclame_tekst4 :
    if len(el)<5:
        print (el.lower())
    else:
        print(el)