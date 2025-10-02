#funkce zkontroluje zda je cislo sude nebo liche
#vypise


# Funkce even_or_odd přijímá jedno číslo a ověří, zda je sudé nebo liché.
# Podle výsledku vytiskne zprávu v češtině.
def even_or_odd(number):
    # Pokud je zbytek po dělení dvěma roven nule, číslo je sudé
    if number % 2 == 0:
        print(f"Číslo {number} je sudé")
    else:
        # Jinak je číslo liché
        print(f"Číslo {number} je liché")


# Ukázkové volání funkce s číslem 5 (očekává se "liché")
even_or_odd(5)

# Ukázkové volání funkce s číslem 1 000 000 (očekává se "sudé")
even_or_odd(1000000)


