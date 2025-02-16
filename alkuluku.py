import sys

# Ohjelma, joka laskee alkulukuja
#! Lisää ohjelmaan funktio, jolla voi laskea käyttäjän syöttämään numeroon saakka alkuluvut. 0-x
# *27.1 lisätty funktion parametrit
# *30.1 ohjelmaan lisätty funktioita.
# *31.1 lisätty ohjelman toisto ja parannettu toimivuutta
# *4.2 estetty muiden kun numeroiden syöttäminen ja superlaskurin implementointi aloitettu

def ohjelma():
    # Käyttäjän valinta
    valinta = input("\nSyötä 1. jos haluat tietää, onko jokin tietty luku alkuluku \nSyötä 2. jos haluat laskea alkulukuja tiettyyn numeroon saakka\n")
    
    # Väärän syötteen estäminen
    if valinta not in ["1", "2"]:
        print("Anna 1 tai 2")
        return ohjelma()

    # funktio joka laskee onko yksittäinen numero alkuluku
    def alkulaskuri(numero):
        vertailu = 2
        if numero == 1:
            print("1 on alkunumero")
        else:
            while vertailu < numero:
                if numero % vertailu == 0:
                    print(f"\n{numero} ei ole alkuluku\n")
                    return
                else:
                    vertailu += 1
            print(f"\n{numero} on alkuluku!!!\n")
   
    # funktio, joka laskee alkulujuja 0 - käyttäjän valitsema luku
    def superlaskuri(numero):
        print(f"Annoit numeron {numero} mutta superlaskuria ei ole toteutettu vielä 💩!\n")
        pituus = 1
        while pituus <= numero:
            vertailu = 1
            break
            
                


    # Käyttäjän inputti ja laskuohjelman valinta
    def kysely():
        while True:                         # Käyttäjän syötteen kelvollisuuden tarkistus
            syöte = input("Anna numero: ")
            if syöte.isnumeric():
                numero = int(syöte)
                if valinta == "1":
                    alkulaskuri(numero)
                else:
                    superlaskuri(numero)
                break
            else:
                print("Anna numero!!!")

        # Jos syöte on 1 -> kysyy inputtia joka syötetään alkulaskuriin
    if valinta == "1" or valinta == "2":
        kysely()
    

    print("Haluatko laskea lisää alkulukuja?")

    # Käyttäjältä kysytään haluaako tämä laskea lisää alkulukuja
    while True:
        uusikierros = input("\nY -> Kyllä\nN -> Poistu\n")
        if uusikierros.lower() not in ["y", "n"]:
            continue
        else:
            break

    # Ohjelman aloittaminen alusta tai lopetus
    if uusikierros.lower() == "y":
        ohjelma()
    else:
        print("\nHeipähei\n")
        sys.exit()

ohjelma()
        