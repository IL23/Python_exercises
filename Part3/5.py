#  Izveidot ģeneratora funkciju, kas ģenerē pirmskaitļus
#  (skaitļi kas dalās tikai ar 1 vai ar sevi, 0 un 1 nav pirmskaitļi).


def prime_numbers(start, stop):
    if start < 2:
        start = 2
    for i in range(start, stop + 1):
        is_prime_num = True
        for j in range(start, i):
            if i % j == 0:
                is_prime_num = False
                break
        if is_prime_num:
            yield i


first = int(input("Start: "))
last = int(input("End: "))

for num in prime_numbers(first, last):
    print(num)
