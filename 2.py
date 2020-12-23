# 2.     Izveidot programmu, kura prasa lietotājam ievadīt cilindra rādiusu un tā augstumu, tiek aprēķināts cilindra
# laukums un tilpums. Rezultāts tiek parādīts konsolē.

height = int(input("Enter the height: "))
radius = int(input("Enter the radius: "))
print("Volume:", 3.14 * radius * radius * height)
print("Area:", 2 * (3.14 * radius * radius) + height * (2 * 3.14 * radius))