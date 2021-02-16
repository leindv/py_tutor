# Для копирования списка используется конструкция [:]
# В точке 1 создается список элементов с именем my_foods.
# В 2 создается другой список.
my_foods = ['pizza', 'falafel', 'carrot cake'] #1
friend_foods = my_foods[:] #2
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
