# 3.Izveidot programmu, kura prasa lietotājam sekunžu skaitu.
# Sekundes tiek pārveidotas par “x hours y minutes z seconds” tipa tekstu.
# Rezultāts tiek parādīts konsolē.

s = int(input("Seconds: "))
hours = int(s / 3600)
min = int((s - hours * 3600) / 60)
sec = s - hours * 3600 - min * 60
print(hours, "hours", min, "minutes", sec, "seconds")
