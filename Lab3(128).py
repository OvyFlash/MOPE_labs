"""
1. Скласти матрицю планування для дробового трьохфакторного експерименту. Провести
експеримент в усіх точках факторного простору, повторивши N експериментів, де N – кількість
експериментів (рядків матриці планування) в усіх точках факторного простору – знайти значення
функції відгуку У. Значення функції відгуку знайти у відповідності з варіантом діапазону,
зазначеного далі (випадковим чином).

2. Знайти коефіцієнти лінійного рівняння регресії. Записати лінійне рівняння регресії.

3. Провести 3 статистичні перевірки.
"""
"""
x1min = -15
x1max = 30
x2min = 30
x2max = 80
x3min = 30
x3max = 35

"""

import random
import numpy as np
import math


def main (m=3, Gt=0.7679):
    def wrapper (func):
        def inner_func (*args, **kwargs):
            print(f"{'':-^49}\nВиконаємо перевірку")
            func(*args)
            print(f"{'':-^49}")

        return inner_func

    x1min = -15
    x1max = x2min = x3min = 30
    x2max = 80
    x3max = 35

    x1_cod = [-1, -1, 1, 1]
    x2_cod = [-1, 1, -1, 1]
    x3_cod = [-1, 1, 1, -1]

    ymin = 200 + round((x1max + x2max + x3max) / 3)
    ymax = 200 + round((x1min + x2min + x3min) / 3)

    m = m
    X1 = [x1min, x1min, x1max, x1max]
    X2 = [x2min, x2max, x2min, x2max]
    X3 = [x3min, x3max, x3max, x3min]
    X_ALL = [X1, X2, X3]

    Y_ALL = [[random.randint(ymax, ymin) for _ in range(4)] for _ in range(m)]

    # Кодовані значення
    print("Кодовані значення Х")
    print("|{0: ^3}|{1: ^3}|{2: ^3}|\n".format("X1", "X2", "X3") +
          "{:-^13}\n".format("") +
          "|{0: ^3}|{1: ^3}|{2: ^3}|\n".format(x1_cod[0], x2_cod[0], x3_cod[0]) +
          "{:-^13}\n".format("") +
          "|{0: ^3}|{1: ^3}|{2: ^3}|\n".format(x1_cod[1], x2_cod[1], x3_cod[1]) +
          "{:-^13}\n".format("") +
          "|{0: ^3}|{1: ^3}|{2: ^3}|\n".format(x1_cod[2], x2_cod[2], x3_cod[2]) +
          "{:-^13}\n".format("") +
          "|{0: ^3}|{1: ^3}|{2: ^3}|\n".format(x1_cod[3], x2_cod[3], x3_cod[3]) +
          "{:-^13}\n".format(""))

    # Натуральні значення
    def y_string (allYValues):
        final = ""
        for i in range(len(list(allYValues))):
            final += "{0: ^3}|".format(list(allYValues)[i])
        return final

    def re_zip (allYValues):
        l = [[0 for _ in range(len(allYValues))] for _ in range(len(allYValues[0]))]
        for i in range(len(allYValues)):
            for j in range(len(allYValues[i])):
                l[j][i] = allYValues[i][j]
        return l

    print(f"Натуральні значення з m = {m}")
    print("|{0: ^3}|{1: ^3}|{2: ^3}".format("X1", "X2", "X3"), end="")
    for i in range(m):
        print(f"|Y{i+1} ", end="")
    print("|")

    for i in range(4):
        print(
            "|{0: ^3}|{1: ^3}|{2: ^3}|".format(X1[i], X2[i], X3[i]) +
            y_string(re_zip(Y_ALL)[i]))

    # Знайдемо середні значення функції відгуку за рядками
    Y_ALL_ZIPPED = re_zip(Y_ALL)  # NEW

    y_averages = list(map(lambda x: sum(x) / len(x), Y_ALL_ZIPPED))  # NEW

    mx1 = sum(X1) / 4
    mx2 = sum(X2) / 4
    mx3 = sum(X3) / 4

    my = sum(y_averages) / len(y_averages)  # NEW

    a = [0 for _ in range(len(X_ALL))]  # NEW
    for i in range(len(X_ALL)):  # NEW
        for j in range(len(X_ALL[i])):
            a[i] += X_ALL[i][j] * y_averages[j]
        a[i] /= 4

    a11 = (X1[0] * X1[0] + X1[1] * X1[1] + X1[2] * X1[2] + X1[3] * X1[3]) / 4
    a22 = (X2[0] * X2[0] + X2[1] * X2[1] + X2[2] * X2[2] + X2[3] * X2[3]) / 4
    a33 = (X3[0] * X3[0] + X3[1] * X3[1] + X3[2] * X3[2] + X3[3] * X3[3]) / 4
    a12 = a21 = (X1[0] * X2[0] + X1[1] * X2[1] + X1[2] * X2[2] + X1[3] * X2[3]) / 4
    a13 = a31 = (X1[0] * X3[0] + X1[1] * X3[1] + X1[2] * X3[2] + X1[3] * X3[3]) / 4
    a23 = a32 = (X2[0] * X3[0] + X2[1] * X3[1] + X2[2] * X3[2] + X2[3] * X3[3]) / 4

    left = np.array([[1, mx1, mx2, mx3],
                     [mx1, a11, a12, a13],
                     [mx2, a12, a22, a23],
                     [mx3, a13, a23, a33]])

    right = np.array([my, a[0], a[1], a[2]])  # UPD
    b = np.linalg.solve(left, right)

    print("Отримане рівняння регресії")
    print(f"y = {b[0]:.2f} + {b[1]:.2f}*x1 + {b[2]:.2f}*x2 + {b[3]:.2f}*x3")

    @wrapper
    def check (allX, coef, y_av):
        for i in range(len(allX[0])):
            print(
                f"{coef[0]:.2f} + {coef[1]:.2f}*{allX[0][i]} + {coef[2]:.2f}*{allX[1][i]} + {coef[3]:.2f}*{allX[2][i]} = ",
                end=" ")
            print(coef[0] + coef[1] * allX[0][i] + coef[2] * allX[1][i] + coef[3] * allX[2][i])
        print(y_av)

    check(X_ALL, b, y_averages)

    # Використання матриці з нормованими значеннями факторів
    # Знайдемо значення дисперсії по рядках

    disp = [0 for _ in range(4)]  # NEW
    for i in range(len(Y_ALL_ZIPPED)):
        for j in range(len(Y_ALL_ZIPPED[i])):
            disp[i] += (Y_ALL_ZIPPED[i][j] - y_averages[i]) ** 2
        disp[i] /= len(Y_ALL_ZIPPED[0])

    Gp = max(disp) / sum(disp)

    f1 = m - 1
    f2 = N = 4
    # Рівень значимості 0.95
    Gt = Gt
    if Gp < Gt:
        print("Дисперсія однорідна")
    else:
        print("Дисперсія неоднорідна")
        m = int(input("Введіть нове значення m: "))
        Gt = float(input("Введіть значення Gt для нового m: "))
        main(m, Gt)
        pass

    # Оцінимо значимість коефіцієнтів регресії згідно критерію Стюдента

    Sb = sum(disp) / N
    SSb = Sb / (N * m)

    notSsb = math.sqrt(SSb)

    beta0 = (y_averages[0] * 1 + y_averages[1] * 1 + y_averages[2] * 1 + y_averages[3] * 1) / 4
    beta1 = (y_averages[0] * (-1) + y_averages[1] * (-1) + y_averages[2] * 1 + y_averages[3] * 1) / 4
    beta2 = (y_averages[0] * (-1) + y_averages[1] * 1 + y_averages[2] * (-1) + y_averages[3] * 1) / 4
    beta3 = (y_averages[0] * (-1) + y_averages[1] * 1 + y_averages[2] * 1 + y_averages[3] * (-1)) / 4

    t0 = abs(beta0) / notSsb
    t1 = abs(beta1) / notSsb
    t2 = abs(beta2) / notSsb
    t3 = abs(beta3) / notSsb
    all_T = [t0, t1, t2, t3]
    f3 = f1 * f2
    Tcr = {1: 12.71, 2: 4.303, 3: 3.184, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228,
           11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145,
           15: 2.131, 16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086, 21: 2.080, 22: 2.074, 23: 2.069, 24: 2.064,
           25: 2.060, 26: 2.056, 27: 2.052,
           28: 2.048, 29: 2.045, 30: 2.042}

    for i in range(4):
        if all_T[i] < Tcr.get(f3, 1.960):
            print(f"Приймаємо b{i} при рівні значимості 0.05 незначні. Виключаємо його з рівняння")
            b[i] = 0

    print(f"y = {b[0]} + {b[1]}*x1 + {b[2]}*x2 + {b[3]}*x3")

    yy1 = b[0] + b[1] * X1[0] + b[2] * X2[0] + b[3] * X3[0]
    yy2 = b[0] + b[1] * X1[1] + b[2] * X2[1] + b[3] * X3[1]
    yy3 = b[0] + b[1] * X1[2] + b[2] * X2[2] + b[3] * X3[2]
    yy4 = b[0] + b[1] * X1[3] + b[2] * X2[3] + b[3] * X3[3]

    # Критерій Фішера
    d = 2
    f4 = N - d
    Sad = ((yy1 - y_averages[0]) ** 2 + (yy2 - y_averages[1]) ** 2 + (yy3 - y_averages[2]) ** 2 + (yy4 - y_averages[3]) ** 2) * (m / (N - d))
    Fp = Sad / Sb
    # Ft берем із таблиці F3 рядoк F2 стовпець
    Ft = float(input(f"Оберіть у таблиці розподілу Фішера значення {f3} рядка і {f2} стовпця: "))
    if Fp > Ft:
        print("Fp=", round(Fp, 2), ">Ft", Ft, "Рівняння неадекватно оригіналу")
    else:
        print("Fp=", round(Fp, 2), "<Ft", Ft, "Рівняння адекватно оригіналу")


main()
