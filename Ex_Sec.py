# n = int(input('Введите число: '))
# result = 1
# while n > 1:
#     result *= n
#     n -= 1
# print(result)


# n = int(input("Введите число: "))
# my_fib = [0, 1]
# while n > my_fib[-2]:
#     if my_fib[-1] == n:
#         print(len(my_fib))
#     my_fib.append(my_fib[-1] + my_fib[-2])
# if my_fib[-2] != n:
#     print(-1)
    
# import random
# n = int(input("Введите число от 1 до 100: "))
# temperature_list = [random.randint(-50, 50) for _ in range(n)]
# result = 1
# counter = 0
# for i in temperature_list:
#     if i > 0:
#         counter += 1
#         if counter > result:
#             result = counter
#     else:
#         counter = 0
# print(result)


# import random
# n = int(input("Введите число арбузов: "))
# weight_watermelons_list = [random.randint(1, 11) for _ in range(n)]
# max_weight = max(weight_watermelons_list)
# min_weight = min(weight_watermelons_list)
# print(f'Самый легкий арбуз для тёщи весит {min_weight} кг., а самый тяжелый, для себя, {max_weight} кг.')

# nums = [1, 1, 2, 0, -1, 3, 4, 4]
# result = len(set(nums))
# print(result)

# nums = [1, 2, 3, 4, 5] 
# k = int(input("Введите ширину сдвига: "))
# div = k % len(nums)
# result = nums[div:] + nums[:div]
# print(*result)


# my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# result = set()
# for a in my_list:
#     value = list(a.values())
#     result.add(value[0])
# print(result)

# import random
# n = int(input("Введите длинну списка: "))
# my_list = [random.randint(1, 101) for _ in range(n)]
# counter = 0
# for i in range(1, len(my_list)):
#     if my_list[i] > my_list[i-1]:
#         counter += 1
# print(counter)


# n = int(input("Введите количество холодильников: "))
# words = []
# name_virus = "anton"
# for _ in range(n):
#     words.append(input())

# for i in range(n):
#     word = words[i]
#     anton_index = 0
#     for letter in word:
#         if letter == name_virus[anton_index]:
#             anton_index += 1
#             if anton_index == 5:
#                 print(i + 1, end=" ")
#                 break

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*


# def simple(n, div = 2):
#     if n == 2 or div ** 2 > n:
#         return True
#     elif n % div == 0:
#         return False
#     return simple(n, div + 1)

# print(simple(6))

# def pal(s):
#     if len(s) <= 1:
#         return True
#     elif s[0] == s[-1]:
#         return pal(s[1:-1])
#     return False

# print(pal("215132"))

# def divs(n, div = 1):
#     result = []
#     while div < n:
#         if n % div == 0:
#             result.append(div)
#             div += 1
#         else:
#             div += 1
#     return result

# def summ(my_list):
#     result = 0
#     for i in my_list:
#         result += i
#     return result

# k = int(input())
# for j in range(1, k+1):
    


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# result = []
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         result.append(i)
# print(*result, sep="\n")

# a1 = 2         # Первый элемент
# d = 3          # Разность
# n = 4          # Количество элементов

# def progr(a1, d, n):
#     if n == 1:
#         return [a1]
#     else:
#         prev_terms = progr(a1, d, n-1)
#         prev_term = prev_terms[-1]
#         prev_terms.append(prev_term + d)
#         return prev_terms

# progression = progr(a1, d, n)
# print(*progression, sep="\n") 



# def sum_of_divisors(n):
#     s = 1
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             s += i
#             if i != n // i:
#                 s += n // i
#     return s

# k = int(input("Введите число k: "))

# for n in range(2, k+1):
#     m = sum_of_divisors(n)
#     if m > n and sum_of_divisors(m) == n and m <= k:
#         print(n, m)
