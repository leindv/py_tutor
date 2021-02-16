# В точке 1 условие проверяет, что возраст 
# меньше 4. Если это условие истинно, то 
# прога пропускает остальные проверки. 
# Строка 2 является еще одним условием проверки, 
# которая выполняется, если предыдущая прооверка 
# завершилась неудачей. Если ложны эти два условия, 
# то выполняется условие 3.
#
age = 12
if age < 4: #1
    print("Your admission cost is $0.")
elif age < 18: #2
    print("Your admission cost is $25.")
else: #3
    print("Your admission cost is $40.")