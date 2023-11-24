def type_triangle(a, b, c):
    # Vérifier si les longueurs forment un triangle
    if a + b > c and a + c > b and b + c > a:
        # Déterminer le type de triangle
        if a == b == c:
            return "équilatéral"
        elif a == b or a == c or b == c:
            return "isocèle"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "rectangle"
        else:
            return "quelconque"
    else:
        return "Impossible de former un triangle"

# Saisir les longueurs depuis l'utilisateur

a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

    # Appeler la fonction pour déterminer le type de triangle
resultat = type_triangle(a, b, c)

    # Afficher le résultat
print(resultat)

