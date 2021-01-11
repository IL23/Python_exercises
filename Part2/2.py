# 2.     Atrast cik skaitļi norādītajā intervālā dalās ar lietotāja norādīto dalītāju.

start = int(input("Start: "))
end = int(input("End: "))
divider = int(input("Divider: "))
count = 0

for i in range(start, end):
    if i % divider == 0:
        count += 1

print(f"{count} values between {start} and {end} can be divided by {divider}")
