import numpy as np


def guess_the_number(target_number: int, max_number: int) -> int:
    """Функция подбора загаданного числа

    Args:
        target_number (int): Загаданное число
        max_number (int): Верхняя граница диапазона "угадывания" числа

    Returns:
        int: Количество попыток
    """
    min_number = 1 # Нижняя граница диапазона в первой итерации
    generated_number = np.random.randint(min_number, max_number) # Первое сгенерированое число
    count = 1 # Количество попыток
    # print(f'Target number: {target_number}')
    while generated_number != target_number: # Запускается цикл генерации числа, работающий до тех пор, пока сгенериованное число не будет равно загаданному
        # print(f'Generated number: {generated_number}')
        count += 1 # Инкрементация значения количества попыток
        if generated_number > target_number: # Если сгенерированное число больше загаданного
            max_number = generated_number # Верхняя граница диапазона смещается "вниз", до значения сгенерированного числа
        else: # Если сгенерированное число меньше загаданного
            min_number = generated_number # Нижняя граница диапазона смещается "вверх", до значения сгенерированного числа
        generated_number = np.random.randint(min_number, max_number) # Генерация числа с новыми границами диапазона
    # print(f'Number of attempts: {count}')
    return count

def get_statistics(function, count) -> int:
    """Функция статистики, считает среднее число попыток

    Args:
        function ([type]): Исследуемая функция
        count ([type]): Общее число тестов

    Returns:
        int: среднее число попыток
    """
    counts_list = [
        function(target_number=np.random.randint(1, 101), max_number=101) for _ in range(count)
        ] # Список результатов теста
    return f"Среднее число попыток: {np.mean(counts_list)}, при количестве тестов - {count}"

    
if __name__ == "__main__":
    guess_the_number(target_number=np.random.randint(1, 101))
    # print(get_statistics(function=guess_the_number, count=1000))