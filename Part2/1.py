# 1.     Apgriezt pozitīva skaitļa ciparu secību.

num = input("Enter number: ")
numLength = len(num)
revers = ""

for i in range(1, numLength+1):
    revers += num[numLength-i]

print(revers)
