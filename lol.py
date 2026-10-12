import math

print("=== Инженерный калькулятор ===")
print("Операции: +, -, *, /, sqrt (корень), sin, cos, log")
print("Для выхода введите 'q'")

while True:
    op = input("\nВведите операцию: ")

    if op == 'q':
        print("Работа завершена.")
        break

    if op in ('+', '-', '*', '/'):
        x = float(input("Первое число: "))
        y = float(input("Второе число: "))

        if op == '+':
            print(f"Результат: {x + y}")
        elif op == '-':
            print(f"Результат: {x - y}")
        elif op == '*':
            print(f"Результат: {x * y}")
        elif op == '/':
            if y != 0:
                print(f"Результат: {x / y}")
            else:
                print("Ошибка: деление на ноль!")

    elif op in ('sqrt', 'sin', 'cos', 'log'):
        x = float(input("Введите число: "))

        if op == 'sqrt':
            if x >= 0:
                print(f"Результат: {math.sqrt(x)}")
            else:
                print("Ошибка: корень из отрицательного числа!")
        elif op == 'sin':
            print(f"Результат: {math.sin(math.radians(x))}")
        elif op == 'cos':
            print(f"Результат: {math.cos(math.radians(x))}")
        elif op == 'log':
            if x > 0:
                print(f"Результат: {math.log(x)}")
            else:
                print("Ошибка: логарифм неположительного числа!")
    else:
        print("Неизвестная операция.")