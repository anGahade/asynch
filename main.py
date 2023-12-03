"""
Завдання:
Вам дано великий список цілих чисел. Ваше завдання полягає в тому,
щоб розподілити цей список на дві приблизно рівні частини і
використовувати два окремі процеси для підрахунку кількості парних чисел в кожній з цих частин.
Вимоги:
1. Використовувати модуль `multiprocessing` для створення процесів.
2. Результати обох процесів повинні бути підсумовані і виведені.
"""
from multiprocessing import Process, Value, Array, Lock


def count_even_numbers(numbers, result, lock):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1

    with lock:
        result.value += count


if __name__ == "__main__":
    numbers_list = list(range(1, 251))
    half_of_list = len(numbers_list) // 2

    first_half = numbers_list[:half_of_list]
    second_half = numbers_list[half_of_list:]

    result_first_half = Value('i', 0)
    result_second_half = Value('i', 0)
    lock = Lock()

    process_first_half = Process(target=count_even_numbers, args=(first_half, result_first_half, lock))
    process_second_half = Process(target=count_even_numbers, args=(second_half, result_second_half, lock))

    process_first_half.start()
    process_second_half.start()

    process_first_half.join()
    process_second_half.join()

    total_even_numbers = result_first_half.value + result_second_half.value

    print("Кількість парних чисел в першій половині:", result_first_half.value)
    print("Кількість парних чисел в другій половині:", result_second_half.value)
    print("Загальна кількість парних чисел:", total_even_numbers)


