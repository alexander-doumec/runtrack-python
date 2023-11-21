# Parcourir les nombres de 0 à 100
for i in range(101):
    # Exclure les nombres 26, 37 et 88
    if i not in [26, 37, 88]:
        print(i)