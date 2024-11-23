reddito_imp = -1

while reddito_imp < 0:
    reddito_imp = float(input("Inserisci il tuo reddito: "))

imposta = 0.0
aliquota12 = 0.12
aliquota18 = 0.18
aliquota27 = 0.27
aliquota48 = 0.48
aliquota60 = 0.60

if reddito_imp > 100000:
    imposta += (reddito_imp - 100000) * aliquota60
    reddito_imp = 100000
    print(f"Imposta: {imposta} euro.")
    
if 60000 < reddito_imp <= 100000:
    imposta += (reddito_imp - 60000) * aliquota48
    reddito_imp = 60000 
    print(f"Imposta: {imposta} euro.")
    
if 35000 < reddito_imp <= 60000:
    imposta += (reddito_imp - 35000) * aliquota27
    reddito_imp = 35000
    print(f"Imposta: {imposta} euro.")
    
if 20000 < reddito_imp <= 35000:
    imposta += (reddito_imp - 20000) * aliquota18
    reddito_imp = 20000
    print(f"Imposta: {imposta} euro.")
    
if 10000 < reddito_imp <= 20000:
    imposta += (reddito_imp - 10000) * aliquota12
    print(f"Imposta: {imposta} euro.")

print(f"Sul tuo reddito verranno detratte {imposta} euro di imposta.")
