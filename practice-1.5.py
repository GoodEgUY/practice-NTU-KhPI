num = int(input("Введіть ціле число: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "не є простим числом")
            break
    else:
        print(num, "є простим числом")
else:
    print(num, "не є простим числом")