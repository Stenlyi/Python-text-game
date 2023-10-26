import random

class Postava:
    def __init__(self, jmeno, sila, obrana, zivoty):
        self.jmeno = jmeno
        self.sila = sila
        self.obrana = obrana
        self.zivoty = zivoty

    def __str__(self):
        return f"{self.jmeno} - Síla: {self.sila}, Obrana: {self.obrana}, Životy: {self.zivoty}"

postavy = {
    1: Postava("Pravděpodobnor", 5, 3, 20),
    2: Postava("Elf", 8, 6, 15),
    3: Postava("Gnom", 6, 7, 18),
    4: Postava("Troll", 10, 10, 30),
    5: Postava("Kentaurotaur", 7, 5, 25)
}

smery = ["Sever", "Jih", "Východ", "Západ"]

udalosti = {
    "Sever": "Lesní cesta se zužuje a cítíte zde záhadnou přítomnost.",
    "Jih": "Zaregistrujete starý strom s vyřezávanými runami.",
    "Východ": "Naleznete poklidnou háj s tajemnými svítícími světluškami v noci.",
    "Západ": "Vzduch je naplněn jemnou melodií, která vás vede k kouzelnému jezeru."
}

def dalsi_udalosti():
    udalosti = [
        "Jak pokračujete ve své cestě, Kouzelný les vám odhaluje svou historii.",
        "Starodávné příběhy o hrdinech a mystických bytostech se stanou vaším vodítkem.",
        "Zjistíte, že sbíráte nejen truhly, ale také zachraňujete dědictví lesa.",
        "Každý váš krok přidává novou kapitolu do příběhu tohoto mystického místa.",
        "Kouzlo lesa nezná hranice a vaše role jako jeho ochránce je věčným úkolem.",
        "Ve svém dobrodružství potkáte moudého starého sovu, který sedí na větvi. Předává vám své znalosti o lese a odhaluje skrytá tajemství.",
        "Naleznete skrytý vodopád, který vám dává moc hojení a obnovy.",
        "Kouzelný les je stále se měnícím světem a vy jste nedílnou součástí jeho kouzel.",
        "Vaše cesta pokračuje, když se ponoříte hlouběji do srdce lesa, kde na vás čekají větší tajemství.",
        "Narazíte na mystický portál, který září nadpřirozeným světlem. Vyzývá vás, abyste prozkoumali jeho tajemství, a vy se rozhodnete udělat krok víry.",
        "V portálu objevíte říši jako žádná jiná, plnou hádanek, výzev a nespočtu pokladů.",
        "Každá hádanka, kterou vyřešíte, odemyká část historie lesa a každé vítězství posiluje vaši spojitost s tímto místem."
    ]
    print(random.choice(udalosti))

def herni_funkce():
    print("Další herní funkce:")
    print("1. Hledejte vzácné artefakty a starodávné runy rozeslané po lese.")
    print("2. Rozhodněte se uzavřít spojenectví s mystickými bytostmi nebo zůstat osamoceným hrdinou.")
    print("3. Řešte hádanky a odemykejte tajné průchody a zkratky v lese.")
    volba = input("Vyberte další herní funkci (1/2/3): ")
    print()

    if volba == "1":
        print("Rozhodli jste se hledat vzácné artefakty a runy, hledat skryté znalosti.")
    elif volba == "2":
        print("Raději si vytvoříte spojenectví s mystickými bytostmi a najdete si přátele v lese.")
    elif volba == "3":
        print("Řešení hádanek pro odemčení tajných průchodů je váš způsob, jak se pohybovat v kouzelném lese.")

def matematicky_ukol(nepřítel):
    cislo1 = random.randint(1, 10)
    cislo2 = random.randint(1, 10)
    operace = random.choice(["+", "-", "*"])
    vyraz = f"{cislo1} {operace} {cislo2}"
    vysledek = eval(vyraz)

    print(f"Proti vám stojí nepřítel {nepřítel.jmeno}! Musíte vyřešit tento matematický úkol:")
    print(f"{vyraz} = ?")

    while True:
        odpoved = input("Zadejte správný výsledek: ")
        if odpoved.lstrip('-').isdigit() and int(odpoved) == vysledek:
            print(f"Správně! Porazili jste nepřítele {nepřítel.jmeno}.")
            break
        else:
            print(f"Špatná odpověď. Nepřítel {nepřítel.jmeno} je stále naživu, ale můžete se pokusit znovu.")
            exit(0)

def uvod():
    print("Vítejte v Kouzelném lese!")
    print(f"Skvěle! Vaše postava je {postava.jmeno}.")
    print("Vaše dobrodružství v Kouzelném lese začíná!\n")

def vyber_postavu():
    print("Vyberte si postavu:")
    for cislo, postava in postavy.items():
        print(f"{cislo}. {postava}")

    while True:
        volba = int(input("Zadejte číslo postavy: "))
        if volba in postavy:
             return postavy[volba]
        else:
            print("Neplatná volba. Prosím, vyberte platnou postavu.")

def hra():
    uvod()
    herni_funkce()

    truhly = 0

    while truhly < 10:
        print("\nStojíte na křižovatce v Kouzelném lese. Můžete jít:")
        for i, smer in enumerate(smery, start=1):
            print(f"{i}. {smer}")

        volba_pohybu = int(input("Zadejte číslo směru, kam chcete jít (1-4): "))
        smer = smery[volba_pohybu - 1]

        print(f"\nVydáváte se {smer} a objevíte...")

        dalsi_udalosti()

        if random.random() < 0.2:  
            truhla_nalezena = True
            if truhla_nalezena:
                print("Váš pohled padne na starou truhlu ukrytou pod kameny.")
                truhly += 1
                truhla_nalezena = False 
                print(f"Nyní máte {truhly} truhel.")
        elif random.random() < 0.4:
            nepřítel = random.choice(list(postavy.values()))
            print(f"Z houštiny na tebe vyskočil nepřítel {nepřítel.jmeno}! Musíte bojovat.")

            matematicky_ukol(nepřítel)

            print(f"Porazili jste nepřítele {nepřítel.jmeno} a našli truhlu!")
            truhly += 1

    konec_hry()

if __name__ == "__main__":
    postava = vyber_postavu()
    hra()
    print("Děkuji, že jste si zahráli hru v Kouzelném lese!\n")
    
def konec_hry():
    print("\nGratulace! Úspěšně jste dokončili úkol v Kouzelném lese.")
    print("Sesbírali jste 10 truhel s poklady a objevili srdce lesa.\n")
    print("Les si váš odvážný čin cení a vítá vás jako svého ochránce. Vaše úkoly jsou splněny, děkuji!")