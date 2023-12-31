from abc import ABC, abstractmethod




class Ksztalt(ABC):

    @abstractmethod
    def pole(self):
        pass

    @abstractmethod
    def obwod(self):
        pass


class Prostokat(Ksztalt):

    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def pole(self):
        return self.szerokosc * self.wysokosc

    def obwod(self):
        return 2 * (self.szerokosc + self.wysokosc)


class Kolo(Ksztalt):

    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return 3.14 * self.promien * self.promien

    def obwod(self):
        return 2 * 3.14 * self.promien


# Utworzenie instancji klasy Prostokat i Kolo
prostokat = Prostokat(10, 5)
kolo = Kolo(7)

print(f"Pole prostokąta: {prostokat.pole()}")  # Wydrukuje: Pole prostokąta: 50
print(f"Obwód prostokąta: {prostokat.obwod()}")  # Wydrukuje: Obwód prostokąta: 30
print(f"Pole koła: {kolo.pole()}")  # Wydrukuje wartość pola koła
print(f"Obwód koła: {kolo.obwod()}")  # Wydrukuje wartość obwodu koła

# Próba utworzenia instancji klasy Ksztalt zakończy się błędem, ponieważ jest to klasa abstrakcyjna
# ksztalt = Ksztalt()  # To spowoduje błąd
