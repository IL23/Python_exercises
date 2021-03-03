# Izveidot sarakstu, kur ir skaitļi no 1 līdz 100, kas nedalās ar 3.
numbers = [i for i in range(101) if i % 3 != 0]
print(numbers)

