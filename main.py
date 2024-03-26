from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def szolgaltatasok(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, erkely=False):
        super().__init__(ar, szobaszam)
        self.erkely = erkely

    def szolgaltatasok(self):
        alap_szolgaltatasok = ["Ingyenes Wifi", "TV", "Fürdőszoba"]
        if self.erkely:
            alap_szolgaltatasok.append("Erkély")
        return alap_szolgaltatasok

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, kilatas=False):
        super().__init__(ar, szobaszam)
        self.kilatas = kilatas

    def szolgaltatasok(self):
        alap_szolgaltatasok = ["Ingyenes Wifi", "TV", "Fürdőszoba"]
        if self.kilatas:
            alap_szolgaltatasok.append("Panorámás kilátás")
        return alap_szolgaltatasok

# Példák

egyagyas_szoba = EgyagyasSzoba(60, "101", erkely=True)
print("Egyágyas szoba ára:", egyagyas_szoba.ar)
print("Egyágyas szoba száma:", egyagyas_szoba.szobaszam)
print("Egyágyas szoba szolgáltatások:", egyagyas_szoba.szolgaltatasok())

ketagyas_szoba = KetagyasSzoba(100, "201", kilatas=True)
print("Kétszemélyes szoba ára:", ketagyas_szoba.ar)
print("Kétszemélyes szoba száma:", ketagyas_szoba.szobaszam)
print("Kétszemélyes szoba szolgáltatások:", ketagyas_szoba.szolgaltatasok())