# Для копирования списка используется конструкция [:]
# Здесь данной конструкции (1) нет, поэтому обе переменные 
# связаны одним списком. Т.о. элемент "ice cream" появиться 
# в обеих списках. 
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods #1
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
