# Перемещение элементов между списками.
# Работа начинается с двух списков - непроверенных пользователей 
# (1) и пустого списка. Цикл (2) выпоняется пока в списке 
# unconfirmed_users остаются элементы. Внутри этого списка функция 
# pop() (3) извлекает очередного непроверенного пользователя из 
# конца списка unconfirmed_users. В данном примере последний элемент 
# списка непроверенных пользователей извлекается первым, сохраняется 
# в confirmed_user и добавляется в список проверенных пользователей 
# (4) (то есть извлекается, сщхраняется и добавляется).
# 
#

# Начинаем с двух списков: пользователей для проверки 
# и пустого списка для хранения проверенных пользователей.
unconfirmed_users = ['alice', 'brian', 'candace'] #1
confirmed_users = []

# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users: #2
    confirmed_user = unconfirmed_users.pop() #3

    print(f"Verifying user: {confirmed_user.title()}")
    confirmed_users.append(confirmed_user) #4
# Вывод всех проверенных пользователей.
print('\nThe folling users have been confired:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())