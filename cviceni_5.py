import sys

def  indetifikuj_cisla(data):
    results = []

    for value in data:
        row = []
        for x in value.plit(" , "):
            try:
                x = str(int(x) + 1)
            except ValueError:
                pass
        print(x)

        row.append(x)
    results.append(' , '.join(row))

    return results


if __name__ == "__main__":
    
    
    if len(sys.argv) <= 1:
        print(f"Pouziti: python {sys.argv[0]} jmeno_souboru")
        sys.exit()

    
    file_name = sys.argv[1]
    data = []


    with open(file_name, "r") as file:
        for line in file:
            data.append(line.strip())

    print(data)

    data = indetifikuj_cisla(data)

    print(data)

    #value =  int(value) + 1
