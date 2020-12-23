# 6. Kāda valsts nolēma pāriet uz jaunu naudas sistēmu.
# Vecajā sistēmā bija trīs naudas vienības: dālderis, grasis, santīms.
# Naudas vērtības norādītas zemāk.

dalderi = int(input("Dālderi: "))
grasi = int(input("Graši: "))
sant = int(input("Santīmi: "))
sant_new = dalderi * 37 * 162 + grasi * 37 + sant
dalderi_new = int(sant_new / 100)
sant_new = sant_new - dalderi_new * 100

print("Jaunie dālderi: ", dalderi_new)
print("Jaunie santīmi: ", sant_new)
