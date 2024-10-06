#Задание 1: Поставьте оценку!
#Вася выложил своё новое приложение на платформу для начинающих разработчиков,
#на ней пользователи могут ставить оценку приложению: от −100 до 100. Ему
#захотелось сравнить количество положительных и отрицательных отзывов, для этого
#он заранее отфильтровал все отзывы так, чтобы в конце были те, которые равны нулю.
#Напишите программу, которая находит количество положительных и количество
#отрицательных чисел в последовательности. Последовательность заканчивается на
#числе 0.

import random
n = int(input("Введите число отзывов: "))
feedback_list = [random.randint(-100, 100) for _ in range(n)]

feedback_list.append(0)
feedback_list.sort(key=lambda x: (x == 0, x))
feedback_positive = 0
feedback_negative = 0
counter = 0

while feedback_list[counter] != 0:
    if feedback_list[counter] > 0:
        feedback_positive += 1
        counter += 1
    elif feedback_list[counter] < 0:
        feedback_negative += 1
        counter += 1
    else:
        break
print(f'Количество положительных чисел {feedback_positive}')
print(f'Количество отрицательных чисел {feedback_negative}')
