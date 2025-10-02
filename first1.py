
def cislo_munsi_nez_3(hodnota):
    if hodnota < 3:
        print("Cislo je mensi nez 3")
    elif hodnota > 3:
        print("Cislo je vetsi nez 3")
    else:
        print("Cislo je 3")


if __name__ == "__main__":
    cislo = input("Zadej cislo: ")
    cislo = int(cislo)
    print("cislo je:", {cislo})

    cislo_meensi_nez_3(1)
    cislo_mense_nez_3(cislo) 