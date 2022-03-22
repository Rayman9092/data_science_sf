"""Игра угадай число
компьютер сам загадывает и сам угадывает число"""

import numpy as np


def predict(left=1, right=101):
    """Угадываем число меньше чем за 20 попыток"""
    number = np.random.randint(1, 101)  # компьютер загадывает случайное число
    count = 0

    while True:
        count += 1
        number_predict = (left + right) // 2
        if number == number_predict:
            break
        elif number > number_predict:
            left = number_predict + 1
        else:
            right = number_predict - 1
    return count


def score_game(predict):
    '''За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм'''
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for _ in random_array:
        count_ls.append(predict(1, 101))

    score = int(np.mean(count_ls))
    print("Ваш алгоритм угадывает число в среднем за:{} попыток".format(score))
    return score


score_game(predict)


