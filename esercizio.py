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
    print(f"Imposta: {(reddito_imp - 100000) * aliquota60} euro.")
    reddito_imp = 100000
    
if 60000 < reddito_imp <= 100000:
    imposta += (reddito_imp - 60000) * aliquota48
    print(f"Imposta: {(reddito_imp - 60000) * aliquota48} euro.")
    reddito_imp = 60000 
    
if 35000 < reddito_imp <= 60000:
    imposta += (reddito_imp - 35000) * aliquota27
    print(f"Imposta: {(reddito_imp - 35000) * aliquota27} euro.")
    reddito_imp = 35000
    
if 20000 < reddito_imp <= 35000:
    imposta += (reddito_imp - 20000) * aliquota18
    print(f"Imposta: {(reddito_imp - 20000) * aliquota18} euro.")
    reddito_imp = 20000
    
if 10000 < reddito_imp <= 20000:
    print(f"Imposta: {(reddito_imp - 10000) * aliquota12} euro.")
    imposta += (reddito_imp - 10000) * aliquota12
    

print(f"Sul tuo reddito verranno detratte {imposta} euro di imposta.")
