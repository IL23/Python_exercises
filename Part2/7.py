# 7.     Atrast pāra skaitļa summu norādītājā intervālā.

start = int(input("Start: "))
end = int(input("End: "))
result = 0

if start % 2 != 0:
    start += 1

for i in range(start, end + 1, 2):
    result += i

print(f"Sum: {result}")
