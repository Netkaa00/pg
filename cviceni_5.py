import sys

def  indetifikuj_cisla(data):
    return data


if __name__ == "__main__":
    
    
    if len(sys.argv) <=1:
        print(f"Pouziti: {sys.argv[0]} jmeno_souboru")
        sys.exit()

    
    file_name = sys.argv[1]
    data = []


    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())

    print(data)

    data = indetifikuj_cisla(data)

    print(data)

    value =  int(value)) + 1




