import math

class Couleur:
    def __init__(self, nom, code_hex):
        self.nom = nom
        self.code_hex = code_hex

    def afficher_info(self):
        return "Couleur : {} (code : {})".format(self.nom, self.code_hex)

if __name__ == "__main__":
    jaune = ("jaune" , "#FFFF00")
    bleu = ("bleu" , "#0000FF")
    vert= ("vert" , "#00FF00")

class Figure:
    def __init__(self, nom, couleur):
        self.couleur = couleur
        self.nom = nom

    def afficher_info(self):
        return "figure : {} -{}".format(self.nom, self.Couleur)

    def aire(self):
        return 0

    def perimetre(self):
        return 0

    def afficher_resultats(self):
            print("\n{}".format(self))
            print("\naire : {}".format(self.aire()))
            print("\nperimetre : {}".format(self.perimetre()))

class Cercle(Figure):
    def __init__(self, rayon, couleur):
        self.rayon = rayon
        super().__init__("Cercle", couleur)

    def aire(self):
        return math.pi * self.rayon ** 2
    def perimetre(self):
        return 2 * math.pi * self.rayon

class Rectancle(Figure):
    def __init__(self, longueur, largeur,couleur):
        self.longueur = longueur
        self.largeur = largeur
        super().__init__("Rectancle", Couleur)

    def aire(self):
        return self.longueur * self.largeur
    def perimetre(self):
        return 2* (self.longueur + self.largeur)

class Triangle(Figure):
    def __init__(self, hauteur, base, couleur):
        self.hauteur = hauteur
        self.base = base
        super().__init__("triangle", couleur)

    def aire(self):
        return (self.base * self.hauteur) / 2
    def perimetre(self):
            return self.base + self.hauteur 

             
cercle = Cercle(5, "#FFFF00")
rectancle = Rectancle(4, 6, "#00FF00")
triangle = Triangle(3, 4, "#00FF00")

cercle.afficher_resultats()
rectancle.afficher_resultats()
triangle.afficher_resultats()