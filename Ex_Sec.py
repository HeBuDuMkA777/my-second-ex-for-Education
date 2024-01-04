# n = int(input('Введите число: '))
# result = 1
# while n > 1:
#     result *= n
#     n -= 1
# print(result)

# def fib(n):
#     a, b = 0, 1
#     for __ in range(n):
#         yield a
#         a, b = b, a + b
# return (list(fib(10)))



n = int(input("Введите число: "))
a, b = 0, 1
result = 1
while b <= n:
    a, b = b, a + b
    result += 1
if b == n:
    print(result)
else:
    print(-1)
