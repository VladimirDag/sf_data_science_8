"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def optimal_predict(number):
    """Угадываем число меньше чем за 20 попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
           
    min = 1
    max = 101
    count = 1
    #number = np.random.randint(min, max+1)
    #print(number)
    mid = (min + max) // 2
    
    while number != mid:#если число не угадано
        count +=1
        if number > mid:#если искомое число больше среднего
            min = mid#за нижний край диапозона поиска принимаем среднее
        else:
            max = mid#за верхний край диапозона поиска принимаем среднее
        mid = (min + max) // 2
    return count

def score_game(optimal_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        optimal_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадываем список чисел

    for number in random_array:
        count_ls.append(optimal_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score
score_game(optimal_predict)