
from presentatie import *
from helper import *
import csv
inkomsten={"Aardbeienijs-ijs-totaal": 1000, "Vanille-ijs-totaal": 2000, "Chocolade-ijs-totaal": 1500, "Waterijsjes-totaal": 750}

totaal_inkomsten=som(inkomsten)


presenteer(inkomsten, totaal_inkomsten)

with open('boekhouding.csv', 'w', newline='') as csvfille:
    for key, value in inkomsten.items():
        writer= csv.writer(csvfille, delimiter=';')
        writer.writerow([key, value])