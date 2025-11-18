# job10.py

# 1) Variables initiales
montant = 10000.0   # capital initial en €
taux = 5.0          # taux de rendement annuel en %

def gain_annuel(capital, taux_pct):
    return capital * (taux_pct / 100)

# --- Étape initiale ---
print("=== Situation initiale ===")
print(f"Capital : {montant:.2f} € | Taux : {taux:.2f}%")
print(f"Gain annuel : {gain_annuel(montant, taux):.2f} €")

# 2) Apport de 5 000 € et hausse du taux de 2% (multiplicatif)
montant += 5000
taux *= 1.02
print("\n=== Après apport (+5000€) et hausse du taux (+2%) ===")
print(f"Capital : {montant:.2f} € | Taux : {taux:.2f}%")
print(f"Gain annuel : {gain_annuel(montant, taux):.2f} €")

# 3) Retrait de 10% du montant et baisse du taux de 1% (multiplicatif)
montant *= 0.90
taux *= 0.99
print("\n=== Après retrait (-10%) et baisse du taux (-1%) ===")
print(f"Montant final : {montant:.2f} € | Taux : {taux:.2f}%")
print(f"Nouveau gain annuel : {gain_annuel(montant, taux):.2f} €")