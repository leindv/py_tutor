#  Если подсказка занимает более одной строки,
#  то текст подсказкт можно сохранить в переменной (1) 
#  и пердать эту переменную в функцию input()(2).
#  Здесь оператор += объединяет тескт.
#
promt = "If you tell us you are, we can personalize thr massages you see."
promt += "\nWhat is your first name? " #1

name = input(promt) #2
print(f"\nHello, {name}!")
