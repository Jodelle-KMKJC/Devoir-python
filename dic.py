mots = ["chat", "chat", "oiseau", "oiseau", "chien", "lion", "poule", "poule", "poule", "serpent"]
compteur = {}

for mot in mots:
    if mot in compteur:
        compteur[mot] += 1
    else:
        compteur[mot] = 1

print("nombre d'apparition de chaque mot :")
for mot, nombre in compteur.items():
    print(f"{mot}: {nombre}")

mots_uniques = set(mots)
print("\n mots uniques :")
for mot in mots_uniques:
    print(mot)