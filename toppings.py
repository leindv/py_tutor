# Обработка начинается в строке 1 со списка, содержащего 
# топпинги. Команды в точке 2 проверяют , включает ли заказ 
# конкретные топпинги итд итп etc.... 
requested_toppings = ['mashrooms', 'extra cheese'] #1
if 'mashrooms' in requested_toppings: #2
    print("Adding mashrooms.")
if 'pepperoni' in requested_toppings: #3
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: #4
    print("Adding extra cheese.")
print("\nFinished making your pizza!")       
