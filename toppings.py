# 
# Приводим список как на примере программным 
# способом с проверкой через print.
requested_toppings = ['mashrooms', 'extra cheese'] 
requested_toppings.insert(1, 'green peppers')
print(requested_toppings)

# Выполнение учебного примера.
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")       
