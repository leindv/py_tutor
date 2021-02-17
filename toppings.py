# 
# Приводим список как на примере программным 
# способом с проверкой через print.
requested_toppings = ['mashrooms', 'extra cheese'] 
requested_toppings.insert(1, 'green peppers')
print(requested_toppings)

# Выполнение учебного примера. Здесь прога 
# проверяет каждый элемент списка. В точке 1 
# прога проверяет заказал ли клиент "зеленый 
# перец" и если "да" - выводит сообщение об 
# его отсутсвии. Блок в точке 2 гарантирует, 
# что другие дополнения списка будут включены.
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers': #1
        print('Sorry? we are out of green peppers right now.')
    else: #2
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")       
