
#ЧЕРЕПКОВ АНТОН АЛЕКСАНДРОВИЧ

def main(input: str) -> str:
    try:
        # Разделение входной строки на числа и операцию
        numbers = input.split()
        if len(numbers) != 3:
            raise ValueError("Неверный формат ввода.")

        a = int(numbers[0])
        b = int(numbers[2])

        # Проверка диапазона чисел
        if not 1 <= a <= 10 or not 1 <= b <= 10:
            raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно.")

        # Выполнение операции
        operator = numbers[1]
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Деление на ноль.")
            result = a // b  # Целочисленное деление
        else:
            raise ValueError("Неверная операция.")

        return str(result)

    except ValueError as e:
        print(f"Ошибка: {e}")
        exit()
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
        exit()


if __name__ == "__main__":
    while True:
        input_string = input("Введите арифметическое выражение (например, 5 + 3): ")
        result = main(input_string)
        print(f"Результат: {result}")

