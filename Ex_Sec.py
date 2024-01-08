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