with open("nombre.txt", "w") as fichier:
    for nombre in range (1, 11):
        fichier.write(str(nombre) + "\n")

with open("nombre.txt", "r") as fichier:
    liste = fichier.readlines()

print("les nombres paires sont:")
for ligne in liste:
    nombre = int(ligne.strip())
    if nombre % 2 == 0:
        print(nombre)
