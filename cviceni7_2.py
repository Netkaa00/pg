class chybnasuma(Exception):
    pass

class bankovniucet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0 

    def __str__(self):
        return f"Bankovni ucet({self.jmeno}, zustatek: {self.__zustatek} CZK)"

    def vloz(self, suma = 0): 
        if suma <= 0:
            raise chybnasuma("Suma pro vlozeni musi byt kladna.")    
        self.__zustatek += suma
   
    def vyber(self, suma):
        if suma <= 0:
            raise chybnasuma("Suma pro vlozeni musi byt kladna.")
        if suma > self.__zustatek:
            raise chybnasuma("Nedostatecny zustatek na uctu.")
        self.__zustatek -= suma



if __name__ == "__main__":
    try:    
        ucet = bankovniucet("Alice")
        print(ucet)
        ucet.vloz(100)
        print(ucet)
        ucet.vyber(10)
        print(ucet)

    except chybnasuma as e:
        print(e)