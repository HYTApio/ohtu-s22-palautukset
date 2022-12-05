class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = []
        self.alkioiden_lkm = 0

    def kuuluu(self, n):

        if n in self.ljono:
            return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono.append(n)
            self.alkioiden_lkm += 1
            return True

        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True

        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono

    def yhdiste(a, b):
        yhdiste = IntJoukko()
        for numero in a.ljono + b.ljono:
            yhdiste.lisaa(numero)
        return yhdiste

    def leikkaus(a, b):
        leikkaus = IntJoukko()
        for numero in list(set(a.ljono).intersection(b.ljono)):
            leikkaus.lisaa(numero)
        return leikkaus

    def erotus(a, b):
        erotus = IntJoukko()
        for numero in list(set(a.ljono).difference(b.ljono)):
            erotus.lisaa(numero)
        return erotus

    def __str__(self):
        joukko = str(self.ljono)
        joukko = joukko.replace("[", "")
        joukko = joukko.replace("]", "")
        joukko = "{" + joukko + "}"
        return joukko
