import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(gues_the_number())
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


def gues_the_number():
    predict = np.random.randint(1, 101)
    de = 50
    i = 0
    count = 1
    half = 50
    while i == 0:
        if half < predict:
            half = round(half + de)
            de /= 2
            count += 1
        if half > predict:
            half = round(half - de)
            de /= 2
            count += 1
        if half == predict:
            i += 1
    return count


n = gues_the_number()
score_game(n)