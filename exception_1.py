def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f'Присутствует некорректный тип данных для подсчёта суммы - "{number}" - {type(number).__name__}')
    return (result, incorrect_data)

def calculate_average(numbers):
    average = 0
    try:

        numbers_size = len(numbers)
        sum_numbers, incorrect_count  = personal_sum(numbers)
        average = sum_numbers/(numbers_size - incorrect_count)
    except ZeroDivisionError:
        print(f'В коллекции нет данных для вычислений')
        average = 0
    except TypeError:
        print(f'В аргумент numbers записан некорректный тип данных "{numbers}" - {type(numbers).__name__}'
              f' (не является коллекцией)')
        average = None
    finally:
        return average  # оставил общим для всех блоков

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567, )}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
print(f'Результат 5: {calculate_average([])}')