import numpy as np


def predict(left, right):
    number = np.random.randint(1, 101)
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


print(predict(1, 101))

