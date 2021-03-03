#  Izveidot ģeneratora funkciju,
#  kas ģenerē skaitļa reizinājumus ar skaitļiem no 0 līdz 10

number = int(input("Enter number: "))


def multiply(num):
    for i in range(11):
        yield i*num


for j in multiply(number):
    print(j)
