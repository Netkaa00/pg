
def na_sachovnici(pozice):
    r, s = pozice
    return 1 <= r <= 8 and 1 <= s <= 8


def smer(krok):
    """Vrátí normalizovaný krok (-1, 0, 1) pro každý směr."""
    if krok == 0:
        return 0
    return 1 if krok > 0 else -1


def je_cesta_volna(start, cil, obsazene_pozice):
    """
    Ověří, že všechna mezilehlá pole mezi startem a cílem jsou volná.
    Start je obsazen vlastní figurou – ignorujeme ho. Cílové pole musí být řešeno mimo (nesmí být obsazené).
    Funguje pro ortogonální i diagonální směry.
    """
    r0, c0 = start
    r1, c1 = cil
    dr = r1 - r0
    dc = c1 - c0

    stepr = smer(dr)
    stepc = smer(dc)

    # musí jít buď rovně (věž), diagonálně (střelec), nebo kombinace (dáma) – zde pouze ověříme průchozí směr
    if not ((dr == 0) ^ (dc == 0) or abs(dr) == abs(dc)):  # xor pro rovné směry, nebo diagonála
        return False

    r, c = r0 + stepr, c0 + stepc
    while (r, c) != (r1, c1):
        if (r, c) in obsazene_pozice:
            return False
        r += stepr
        c += stepc
    return True


def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka.get("typ")
    r0, c0 = figurka.get("pozice", (None, None))
    r1, c1 = cilova_pozice

    # 1) Cíl na šachovnici
    if not na_sachovnici(cilova_pozice):
        return False

    # 2) Cílová pozice musí být volná (neřešíme braní; všechny figury jsou "bílé")
    if cilova_pozice in obsazene_pozice:
        return False

    dr = r1 - r0
    dc = c1 - c0
    adr = abs(dr)
    adc = abs(dc)

    # 3) Povolený tvar tahu podle typu figury
    if typ == "pěšec":
        # V tomto úkolu se pěšec pohybuje směrem "dolů" (zvyšuje řádek).
        # Jeden krok vpřed, pokud je volno.
        if dc != 0:
            return False
        if dr == 1:
            return True
        # Dvojkrok z výchozí pozice v 1. řadě (pokud jsou obě pole volná).
        if r0 == 1 and dr == 2:
            # zkontroluj, že mezilehlé pole je volné
            if (r0 + 1, c0) not in obsazene_pozice:
                return True
        return False

    elif typ == "jezdec":
        return (adr, adc) in {(1, 2), (2, 1)}

    elif typ == "věž":
        if dr == 0 or dc == 0:
            return je_cesta_volna((r0, c0), (r1, c1), obsazene_pozice)
        return False

    elif typ == "střelec":
        if adr == adc and adr != 0:
            return je_cesta_volna((r0, c0), (r1, c1), obsazene_pozice)
        return False

    elif typ == "dáma":
        if dr == 0 or dc == 0 or adr == adc:
            return je_cesta_volna((r0, c0), (r1, c1), obsazene_pozice)
        return False

    elif typ == "král":
        return max(adr, adc) == 1

    # Nepodporovaný typ
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
