#5.Zemniekam ir govis, cūkas un vistas. Govīm un cūkām ir pa 4 kājām, vistām – 2.
# Izveidot programmu, kas prasa lietotājam ievadīt cūku, govju un vistu skaitu.
# Tiek aprēķināts kopējais kāju daudzums. Rezultāts tiek izvadīts konsolē.

pigs = int(input("Amount of pigs: "))
cows = int(input("Amount of cows: "))
chickens = int(input("Amount of chickens: "))

print("Total amounts of legs:", 4*(pigs+cows)+2*chickens)