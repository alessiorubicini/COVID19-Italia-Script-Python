'''

Covid19 Tracker with Python

Developed by Alessio Rubicini

Python Version: 3.8.2

'''

# ------------ MODULI --------------

import requests as r
import os
import webbrowser

# ------------ FUNZIONI --------------

# Resoconto ultimi dati
def ultimiDati():

    # File JSON dalla repository GitHub della Protezione Civile
    req = r.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json')
    dati = req.json()[0]

    # Formatta data e ora
    data = str(dati['data']).split('T')

    # Stampa i dati
    print("Ultimo aggiornamento il", data[0] + " alle " + data[1])

    for k, v in dict(dati).items():
        if str(k) != 'data' and str(k) != 'stato':
            print("{K}: {V}".format(K=str(k).title(), V=v))
    


# Ricerca dati per regione
def datiRegione(search):

    # File JSON dalla repository GitHub della Protezione Civile
    req = r.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni-latest.json')
    dati = req.json()

    # Formatta data e ora
    data = str(dati['data']).split('T')

    # Stampa i dati
    print("Ultimo aggiornamento il", data[0] + " alle " + data[1])

    for regione in dati:

        if regione['denominazione_regione'] == str(search) or str(regione['codice_regione']) == str(search):

            for k, v in dict(regione).items():

                if str(k) != 'data' and str(k) != 'stato':
                    print("{K}: {V}".format(K=str(k).title(), V=v))
            


# Ricerca dati per provincia
def datiProvincia(search):

    # File JSON dalla repository GitHub della Protezione Civile
    req = r.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province-latest.json')
    dati = req.json()

    

    for provincia in dati:

        if provincia['denominazione_provincia'] == str(search) or str(provincia['codice_provincia']) == str(search):

            # Formatta data e ora
            data = str(provincia['data']).split('T')

            # Stampa i dati
            print("Ultimo aggiornamento il", data[0] + " alle " + data[1])

            for k, v in dict(provincia).items():

                if str(k) != 'data' and str(k) != 'stato':
                    print("{K}: {V}".format(K=str(k).title(), V=v))


# Menù principale
def main_menu():
    os.system('clear')
    print("---- COVID19 ITALY TRACKER ----")
    print("1. Ultimi dati")
    print("2. Cerca una regione")
    print("3. Cerca una provincia")
    print("4. Fonte dei dati")
    print("5. Esci")



# --------------- MAIN -------------------
scelta = 0

while scelta < 5:

    # Stampa il menù principale
    main_menu()

    # Prende in input la scelta dell'utente
    scelta = int(input("> "))

    # Resoconto ultimi dati
    if scelta == 1:

        ultimiDati()

        input("Premi INVIO per continuare....")


    # Dati regione specifica
    if scelta == 2:
        
        search = input("Inserisci il nome o il codice della regione: ")

        datiRegione(search)
        
        input("Premi INVIO per continuare....")

    # Dati provincia specifica
    if scelta == 3:
        
        search = input("Inserisci il nome o il codice della provincia: ")

        datiProvincia(search)

        input("Premi INVIO per continuare....")

    if scelta == 4:

        webbrowser.open_new_tab('https://github.com/pcm-dpc/COVID-19')


    # Termine programma
    if scelta >= 5:
        print("Grazie per aver utilizzato il software :) ")
        exit()
