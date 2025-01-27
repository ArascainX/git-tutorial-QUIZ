otazky = [
    {
        "vyzva": "V jakem roce vyšla hra League of Legends?",
        "moznosti": ["a) 2008", "b) 2010", "c) 2012", "d) 2014"],
        "odpoved": "b"
    },
    {
        "vyzva": "Kdo je hlavní postava ve hře Zaklínač 3: Divoky hon?",
        "moznosti": ["a) Ciri", "b) Geralt z Rivie", "c) Yennefer", "d) Triss Merigold"],
        "odpoved": "b"
    },
    {
        "vyzva": "Jak se jmenuje syn Kratose v God of War (2018)?",
        "moznosti": ["a) Zeus", "b) Atreus", "c) Ares", "d) Kratos Junior"],
        "odpoved": "b"
    },
    {
        "vyzva": "Které historické období je hlavní kulisou pro Kingdom Come: Deliverance?",
        "moznosti": ["a) Středověká Anglie", "b) Renesanční Italie", "c) České království v 15. století", "d) Středověká Francie"],
        "odpoved": "c"
    },
    {
        "vyzva": "Kdo je hlavni záporák ve hre Spider-Man od Marvelu (2018)?",
        "moznosti": ["a) Norman Osborn", "b) Dr. Octopus", "c) Venom", "d) Kingpin"],
        "odpoved": "d"
    },
    {
        "vyzva": "Jaký je hlavní cíl v League of Legends?",
        "moznosti": ["a) Zničit Nexus", "b) Ovladnout vsechny tři draky", "c) Získat maximum bodů", "d) Porazit všechny hráče na mapě"],
        "odpoved": "a"
    },
    {
        "vyzva": "V Zaklínačovi 3 je Geralt známý svými speciálnímy schopnostmi. Jak se tyto schopnosti nazývaji?",
        "moznosti": ["a) Runy", "b) Znamení", "c) Spells", "d) Magie"],
        "odpoved": "b"
    },
    {
        "vyzva": "Který z těchto bohů je Kratosem v God of War (2018) považován za hlavního nepřítele?",
        "moznosti": ["a) Hades", "b) Odin", "c) Zeus", "d) Thor"],
        "odpoved": "b"
    },
    {
        "vyzva": "V jakem státě se nachazí herní svet Kingdom Come: Deliverance?",
        "moznosti": ["a) Česka republika", "b) NĚmecko", "c) Polsko", "d) Maďarsko"],
        "odpoved": "a"
    },
    {
        "vyzva": "Jaké zbraně pouzívá Kratos v God of War (2018)?",
        "moznosti": ["a) Dvojité sekery", "b) Meč a štít", "c) Meče chaosu", "d) Kladivo a štít"],
        "odpoved": "c"
    }
]


def spustit_kviz(otazky):
    skore = 0
    for otazka in otazky:
        print(otazka["vyzva"])
        for vyber in otazka ["moznosti"]:
            print(vyber)
        odpoved = input ("Zadej svou odpověď (A, B, C, nebo D)").lower()
        if odpoved == otazka["odpoved"]:
            print("Správně!\n")
            skore += 1
        else:
            print("špatná odpověd!!! - Správná odpověď je", otazka["odpoved"], "\n")

    print(f"Tvé celkové skóre je: {skore} z {len(otazky)} možných bodů")

spustit_kviz(otazky)