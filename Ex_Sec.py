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