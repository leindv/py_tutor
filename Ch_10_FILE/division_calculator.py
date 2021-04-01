# Обработка исключений ZeroDivisionError.

# Использование исключений для предотвращения 
# аварийного завершения программы.

# В проге кроме блока try-except есть блок else. 
# Любой код, зависящий от успешного выполнения блока try, 
# размещается в блоке else.

# Прога пытается выполнить операцию деления в блоке (1), 
# который включает только код, способный породить ошибку.
# Любой код, зависящий от успешного выполнения блока try, 
# добавляется в блок else.
# В данном случае, если  операция деления выполняется 
# успешно, блок else используется для вывода результата (3).
# Блок except сообщает проге, как следует поступать при 
# возниконовении ошибки ZeroDivisionError (2) .

print('Give me two numbers, and I will divdide them.')
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ") 
    if first_number == 'q':
        break

    second_number = input("Second number: ") 
    if second_number == 'q':
        break

    try: #1
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: #2
        print("You can not divide by 0!")
    else: #3
        print(answer)
