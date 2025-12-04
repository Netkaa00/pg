class uzivatel:
    def __init__(self, jmeno, telefon, email):
        self.__jmeno = jmeno
        self.telefon = telefon
        self.__email = email

    def __str__(self):
        return f"uzivatel({self.jmeno}, {self.telefon}, {self.email})"
    
    @property
    def jmeno(self):
        return self.__jmeno
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, hodnota):
        
        if hodnota.replace("@", "").replace(".cz", "").islnum():
            raise Exception(f"{hodnota} neni alphanumericky")
        self.__email = hodnota


if __name__ == "__main__":
    u = uzivatel("Jan", "+420777999888", "jan@jcu.cz")

    print (u)
    print(u.jmeno)

  