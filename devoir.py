import math

class Couleur:
    def __init__(self, nom, code_hex):
        self.nom = nom
        self.code_hex = code_hex

    def afficher_info(self);
        return *couleur : {} (code : {})*.format(self.nom, self.code_hex):

            if __name__ == "__main__":
                    rouge = _("rouge" , "red")
                    bleu = _("bleu" , "#0000FF")
                    vert= _("vert" , "#00FF00")
                    jaune= _("jaune" , "#FFFF00")

class Figure:
    def __init__(self, nom, couleur):
        self.couleur = couleur
        self.nom = nom

    def afficher_info(self):
        return "figure : {} -{}".format(self.nom, self.couleur.afficher_info())

    def aire(self):
        return 0

    def perimetre(self):
        return 0

    def afficher_resultats(self):
            print("/n{}".format(self.afficher_info()))
            print("/aire : {}".format:(self.aire()))
            print("/perimetre : {}".format:(self.perimetre()))

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
    def __init__(self, hauteur, base, couleur)
        self.hauteur = hauteur
        self.base = base
        super().__init__("triangle", couleur)

    def aire(self):
        return (self.base * self.hauteur) / 2
        def perimetre(self):
            return self.base + self.hauteur + hypotenuse
    





            

