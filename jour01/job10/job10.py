# Initialisation des variables
montant_initial = 10000.0  # Montant initial de l'investissement
taux_rendement_annuel = 5.0  # Taux de rendement annuel en pourcentage

# Affichage du gain annuel initial
gain_annuel_initial = (taux_rendement_annuel / 100) * montant_initial
print(f"Gain annuel initial : {gain_annuel_initial:.2f} euros")

# Augmentation du capital et du taux de rendement
montant_initial += 5000.0
taux_rendement_annuel += 2.0

# Calcul du nouveau gain avec la nouvelle configuration
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Nouveau gain annuel : {nouveau_gain_annuel:.2f} euros")

# Retrait de 10% du montant total et diminution du rendement de 1%
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1.0

# Calcul du montant final de l'investissement
montant_final = montant_initial + nouveau_gain_annuel
print(f"Montant final de l'investissement : {montant_final:.2f} euros")
