# Здесь придставлен пример, где 
# используются только условия if и elif
# без использования else. Блок else универсален 
# - он обрабатывает все условия, не подходящие 
# ни под одну проверку if и elif.
# 
age = 12
if age < 4: 
    price = 0
elif age < 18: 
    price = 25
elif age < 65: 
    price = 40
elif age >= 65:     
    price = 20
print(f"Your admission cost is ${price}.")
