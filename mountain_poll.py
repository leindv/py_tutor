# Заполнение СЛОВАРЯ данными, введенными пользователем.
# Сначала прога определяет пустой словарь и устанавливаем ФЛАГ.
# Пользователю предлагают ввести имя и название горы, 
# которую он хотел посетить(1). Эта инфо сохранияется в словаре(2),
# после чего прога спрашивает пользователя о продолжении опроса(3).
# Если ответ положителен, то прога снова входит в цикл while, в 
# противном случаеФЛАГ переходит в состояние Fales, цикл перестает 
# выполнятьсяи заверщающий блок кода (4) выводит результат опроса.
#
responses = {}

# Установка ФЛАГА продолжения опроса.
polling_active = True

while polling_active:
    # Запрос имени и ответ пользователя.
    name = input("\nWhat is your name? ") #1
    response = input('Which mountain would you like to climb someday? ')

    # Ответ сохранияется в словаре.
    responses[name]=response # 2

    # Проверка продолжения опроса.
    repeat = input("Would you like to let another person respond? (yes / no) ") #3
    if repeat == 'no':
        polling_active = False

# Опрос завершен, вывести результаты.
print("\n---Poll Results---")
for name, response in responses.items(): #4
    print(f"{name} would like to climb {response}.")
