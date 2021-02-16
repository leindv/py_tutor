# Строка 1 ЧЕТКО читается: если пользователь НЕ входит 
# в черный список (if ... not in ...) banned_users, 
# то прога возвращае True и выполняет строку с отступом.
#
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users: #1
    print(f"{user.title()}, you can post a response if you wish.")
