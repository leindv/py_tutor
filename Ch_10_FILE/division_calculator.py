# Обработка исключений ZeroDivisionError.

# Использование исключений для предотвращения 
# аварийного завершения программы.

# Прога запрашивает у пользователя первое число (1).
# Если пользователь не ввел 'q', прога запрашивает 
# второе чило (2). Здесь также если пользователь не 
# ввел 'q', то прого выпоняет деление первого чила 
# на второе (3).

print('Give me two numbers, and I will divdide them.')
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ") #1
    if first_number == 'q':
        break

    second_number = input("Second number: ") #2
    if second_number == 'q':
        break

    answer = int(first_number) / int(second_number) #3
    print(answer)
