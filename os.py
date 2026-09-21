number = int(input("Введите номер"))
multiply = 1

for i in range(1,11):
    print(f"{number} * {multiply} = {number * multiply}")
    multiply += 11
