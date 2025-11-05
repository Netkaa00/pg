def vydel(citatel, jmenovatel):
    return citatel / jmenovatel

if __name__ == "__main__":

    try:
        cislo1 = None
        while cislo1 is None:
            try:
                cislo1 = int(input("Zadej čitatel: "))

            except Exception:
                print("zadej normalne cislo")

    

    except Exception:
        print("Neco se pokazilo")



    