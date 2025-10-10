

def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    cisla = ["nula", "jedna", "dva", "tri", "ctri", "pet", "sest", "sedum", "osm", "devet",
              "deset", "jedenact", "dvanact", "trinact", "ctrnact", "patnact", "sesnact",
                "sedumnact", "osumnact", "devatenact"]
    desatky = [0, 1, "dvacet", "tricet", "ctiricet", "padesat",
                "sedesat", "sedumdesat", "osumdesat", "devatesat"]
    


    if cislo >= 0 and cislo < 20:
        text = cisla[cislo];

    elif cislo >= 20 and cislo < 100:
        text = desatky[cislo // 10];
        if cislo % 10 != 0:
            text += " " + cisla[cislo % 10];

    elif cislo == 100:
        text = "sto"

    else:
        text = "Cislo je mimo rozsah"
  


    return text

if __name__ == "__main__":
    while True:
        cislo = input("Zadej číslo: ")
        if cislo.lower() == "exit" :
            break
        try:
            cislo = int(cislo)
            text = cislo_text(cislo)
            print(text)
        except ValueError:
            print("jste nezadali cislo" \
            " zadejte cislo, nebo exit pro ukonceni")



    

    