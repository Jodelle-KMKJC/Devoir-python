try:
    x = float(input("entrez le premier nombre:"))
    y = float(input("entrez le second nombre:"))

    reponse = x / y
    print("le quotient est:", reponse)

except ValueError:
    print("Erreur: vous devez entrer des nombres valides")

except ZeroDivisionError:
    print("Erreur: la division par zero est impossible")  

