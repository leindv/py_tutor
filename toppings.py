# Здесь определяется два списка. 
# В 1 содержится перечень доступных 
# топпингов, а 2- список топпиногов, 
# заказанных клиентом. В этот раз каждый 
# элемент из 2-ого списка проверяется по 
# списку доступных топпингов (1).
# В точке 3 идет ПЕРЕБОР элементов списка 2. 
# Внутри цикла прога сначала проверяет, что элементы 
# списка 2 присутсвуют в списке 1 (4) и если топпинг 
# доступен (элементы совпадают), то он (топпинг) 
# добавляется в пиццу. Если нужный элемент списка (2) 
# НЕ ВХОДИТ в список 1, выполняется блок 5.   
# 
available_toppings = ['mashrooms', 'olives', 'green pappers', 'pepperoni', 'pineapple', 'extra cheese'] #1
requested_toppings = ['mashrooms', 'french fries', 'extra cheese'] #2
for requested_topping in requested_toppings: #3
    if requested_topping in available_toppings: #4
        print(f"Adding {requested_topping}.") 
    else: #5
        print(f"Sorry? we don't have {requested_topping}.")
print("\nFinished making your pizza!")
