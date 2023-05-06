def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

lower = int(input("Введіть нижню межу діапазону: "))
upper = int(input("Введіть верхню межу діапазону: "))

primeNumbers = []

for num in range(lower, upper + 1):
    if isPrime(num):
        primeNumbers.append(num)

if len(primeNumbers) == 0:
    print("У вказаному діапазоні немає простих чисел.")
else:
    print("Прості числа у вказаному діапазоні:")
    for prime in primeNumbers:
        print(prime)
    print(f"Кількість простих чисел: {len(primeNumbers)}")