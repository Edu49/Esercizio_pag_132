reddito_imp = -1

while reddito_imp < 0:
    reddito_imp = float(input("Inserisci il tuo reddito: "))

imposta = 0.0
Aliquota12 = 0.12
Aliquota18 = 0.18
Aliquota27 = 0.27
Aliquota48 = 0.48
Aliquota60 = 0.60

if reddito_imp > 100000:
    imposta += (reddito_imp - 100000) * Aliquota60
    print(f"Imposta: {(reddito_imp - 100000) * Aliquota60} euro.")
    reddito_imp = 100000
    
if 60000 < reddito_imp <= 100000:
    imposta += (reddito_imp - 60000) * Aliquota48
    print(f"Imposta: {(reddito_imp - 60000) * Aliquota48} euro.")
    reddito_imp = 60000 
    
if 35000 < reddito_imp <= 60000:
    imposta += (reddito_imp - 35000) * Aliquota27
    print(f"Imposta: {(reddito_imp - 35000) * Aliquota27} euro.")
    reddito_imp = 35000
    
if 20000 < reddito_imp <= 35000:
    imposta += (reddito_imp - 20000) * Aliquota18
    print(f"Imposta: {(reddito_imp - 20000) * Aliquota18} euro.")
    reddito_imp = 20000
    
if 10000 < reddito_imp <= 20000:
    imposta += (reddito_imp - 10000) * Aliquota12
    print(f"Imposta: {(reddito_imp - 10000) * Aliquota12} euro.")
    
print(f"Sul tuo reddito verranno detratte {imposta} euro di imposta.")
