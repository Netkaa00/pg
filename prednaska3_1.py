def faktorial(cislo):

    if cislo == 0 or cislo == 1:
        return 1

    return cislo * faktorial(cislo - 1)

def faktorial2(cislo):
    if cislo == 1 or cislo == 0:
        return 1

    faktorial = 1
    for i in range(2, cislo + 1):
         faktorial *= i
    return faktorial

    


if __name__ == "__main__":

    print(faktorial(5))
    print(faktorial2(5))