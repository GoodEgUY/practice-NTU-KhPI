numList = []
n = 7 
for i in range(n):
    num = int(input(f"Введіть число {i+1}: "))
    numList.append(num)

print("Список введених чисел:", numList)

maxNum = numList[0]
minNum = numList[0]
for num in numList:
    if num > maxNum:
        maxNum = num
    if num < minNum:
        minNum = num

print("Максимальне число:", maxNum)
print("Мінімальне число:", minNum)

sumNum = 0
for num in numList:
    sumNum += num
average = sumNum / n

print("Середнє арифметичне:", average)

ascList = sorted(numList)
print("Список введених чисел у зростаючому порядку:", ascList)

descList = sorted(numList, reverse=True)
print("Список введених чисел у спадаючому порядку:", descList)

numBigger5 = [num for num in numList if num > 5]
print("Список чисел, більших за 5:", numBigger5)
