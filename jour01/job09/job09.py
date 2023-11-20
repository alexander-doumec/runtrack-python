nom="Nike"
prix_unitaire= 4000
quantité_stock=40




print("Informations du produit")
print(f"Nom du produit: {nom}")
print(f"Prix unitaire: {prix_unitaire} €")
print(f"Quantité en stock: {quantité_stock}")

quantite_achetee = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))

# Mettre à jour le stock
quantité_stock += quantite_achetee

# Mise à jour du prix après inflation de 10%
prix_unitaire *= 1.10

# Affichage des informations mises à jour du produit
print("\nInformations mises à jour du produit :")
print(f"Nom du produit : {nom}")
print(f"Prix unitaire après inflation : ${prix_unitaire:.2f}")
print(f"Quantité en stock après achat : {quantité_stock} unités")