class osoba:
    def __init__(self, name, age):
        self.jmeno = name
        self.vek = age

    def __str__(self):
        return f"Osoba({self.jmeno}, {self.vek})"
    
    def pridej_rok(self):
        self.vek += 1
        
    

class student(osoba):
    def __init__(self, name, age, rocnik = 1):
        super().__init__(name, age)
        self.rocnik = rocnik
        
    def __str__(self):
        return f"Student({self.jmeno} ma {self.vek} let studuje {self.rocnik} rocnik)"
    
    def pridej_rok(self):
        super().pridej_rok()
        if self.rocnik < 5:
            self.rocnik += 1

    
class uctel(osoba):
    def __init__(self, name, age, roky_praxe = 0):
        super().__init__(name, age)
        self.roky_praxe = roky_praxe
    def __str__(self):
        return f"Uctel({self.jmeno} ma {self.vek} let a {self.roky_praxe} let praxe)"
    
    def pridej_rok(self):
        super().pridej_rok()
        if self.roky_praxe > 5:
            self.roky_praxe += 1

class udrbar(osoba):
    def __str__(self):
        return f"Udrbar({self.jmeno} ma {self.vek} let a specializuje se na {self.specializace})"
    

        
    
if __name__ == "__main__":

    student1 = student("Alice", 19, 4)
    student2 = student("Bob", 20, 3)
    ucitel1 = uctel("Dr. Smith", 45, 20)
    ucitel2 = uctel("Prof. Johnson", 50)
    udrbar1 = udrbar("Tomas", 55)

    osoby = [student1, ucitel1, udrbar1]


    for i in range(10):
        for osoba in osoby:
            osoba.pridej_rok()

    
    for osoba in osoby:
        print(osoba)
