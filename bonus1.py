caractere = "Entrer un text:"

liste = []

while len(liste) < 3:
    montext = input(caractere)
    liste.append(montext.title())
print(liste)