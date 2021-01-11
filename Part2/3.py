# 3.     Aprēķināt skaitļu summu lietotāja norādītajā intervālā.
# Ja skaitlis dalās ar 13 vai ne-dalās ar 4 un ir trīsciparu skaitlis, tad skaitlis nav jāpievieno summai,
# bet, ja skaitlis ir četrciparu skaitlis un dalās ar 7, un dalās ar 1000, tad summas skaitīšana ir jāpārtrauc.


start = int(input("Start: "))
end = int(input("End: "))
result = 0

for i in range(start, end + 1):
    if i % 13 == 0 or i % 4 and (len(str(i)) == 3):
        continue
    elif len(str(i)) == 4 and i % 7 == 0 and i % 1000 == 0:
        print("Last: ", i)
        break
    else:
        result += i

print(f"Sum: {result}")


