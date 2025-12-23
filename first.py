def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        print(f"{cislo} je sudé číslo")
    else:
        print(f"{cislo} je liché číslo")


if __name__ == "__main__":

    cislo = input("Zadej číslo: ")
    sudy_nebo_lichy(int(cislo))


