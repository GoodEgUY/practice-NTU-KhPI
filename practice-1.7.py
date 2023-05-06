def factorial(n):
    if n < 0:
        return "Факторіал від'ємного числа обчислити неможна."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Введіть число: "))
result = factorial(num)

if type(result) == str:
    print(result)
else:
    print(f"Факторіал числа {num} дорівнює {result}.")
